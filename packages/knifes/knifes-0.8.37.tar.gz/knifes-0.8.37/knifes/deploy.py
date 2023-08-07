import os
import sys
import time
from datetime import datetime, timedelta
from .file import read_file
from .shell import *
systemd_template = """[Unit]
Description={Description}.gunicorn.service
ConditionPathExists={ConditionPathExists}
After=network.target

[Service]
PIDFile={PIDFile}
ExecStart={ExecStart}

[Install]
WantedBy=multi-user.target"""


def print_help(project_dir, app_name):
    print('reload      --reload gunicorn\n'
          'start       --start gunicorn\n'
          'log n       --read gunicorn last log\n'
          'modules     --install modules\n'
          'knifes      --force install latest knifes\n'
          'autostart   --autostart at boot\n'
          'celery [start | restart | stop]\n'
          'celerybeat [start | restart | stop]\n\n'
          f'systemctl status {app_name}.gunicorn.service\n\n'
          'activate virtual environment cmd:\n\n'
          f'source {project_dir}venv/bin/activate')


def main_script(chdir, logdir, app_name, project_name=None):
    if not project_name:
        project_name = app_name

    args = sys.argv[1:]
    if not args:
        print_help(chdir, app_name)
    elif args[0] == 'reload':
        reload_gunicorn(chdir, logdir)
    elif args[0] == 'modules':
        install_modules(chdir)
    elif args[0] == 'log':
        line_count = 10 if len(args) == 1 else args[1]
        read_last_log(logdir, line_count)
    elif args[0] == 'start':
        start_gunicorn(chdir, logdir, app_name)
    elif args[0] == 'knifes':
        install_latest_knifes(chdir)
    elif args[0] == 'autostart':
        autostart_at_boot(chdir, logdir, app_name)
    elif args[0] == 'celery':
        celery(chdir, logdir, project_name, args[1], False)
    elif args[0] == 'celerybeat':
        celery(chdir, logdir, project_name, args[1], True)
    else:
        print_help(chdir, app_name)


def celery(project_dir, log_dir, project_name, operate, is_beat=False):
    if operate not in ('restart', 'stop', 'start'):
        print_err('not supported operate, only supports [start | restart | stop]')
        return

    type_ = 'beat' if is_beat else 'worker'
    pid_file = f'{log_dir}celery_{type_}.pid'
    log_file = f'{log_dir}celery_{type_}{"" if is_beat else "%I"}.log'

    # stop
    if operate in ('restart', 'stop'):
        pid = read_file(pid_file).strip()
        if not pid:
            print_err(f'restart/stop {type_} failed，pid not exists:{pid_file}')
            return
        exec_shell(f'kill -KILL {pid}')
        print_succ(f'stopped old {type_} process: {pid}')

    # start new process
    if operate in ('restart', 'start'):
        cmd = f'cd {project_dir} && venv/bin/celery -A {project_name} {type_} --pidfile={pid_file} --logfile={log_file} --loglevel=INFO --detach'
        if not is_beat:
            cmd += ' --concurrency=1'
        # 判断是否已启动
        succ, err = exec_shell(f"pgrep -f '{cmd}'")
        if succ:
            print_err('it is currently started, please restart it through the restart command')
            return
        succ, err = exec_shell(cmd)
        print_succ(succ)
        print_err(err)
        time.sleep(1)
        print_succ(f'new {type_} process: {read_file(pid_file).strip()}')


def install_latest_knifes(project_dir):
    cmd = 'source {}venv/bin/activate && pip install knifes --index-url https://pypi.python.org/simple -U'.format(project_dir)
    succ, err = exec_shell(cmd)
    print_succ(succ)
    print_err(err)


def install_modules(project_dir):
    cmd = 'source {}venv/bin/activate && pip install -r {}requirements.txt'.format(project_dir, project_dir)
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ret.returncode != 0:
        print_err(ret.stderr.decode())
        raise SystemExit
    print_succ(ret.stdout.decode())
    print_succ(ret.stderr.decode())  # warning message


def read_last_log(log_dir, line_count):
    succ, err = exec_shell('tail -{} {}error.log'.format(line_count, log_dir))
    print_succ(succ)
    print_err(err)
    return succ, err


def autostart_at_boot(project_dir, log_dir, app_name):
    """设置开机自启动"""
    systemd_conf_filepath = f'/etc/systemd/system/{app_name}.gunicorn.service'
    if os.path.exists(systemd_conf_filepath):  # 已设置
        print_succ('开机自启动配置已存在')
        return

    python_binary = f'{project_dir}venv/bin/python'
    pid_file = f'{log_dir}pid.pid'
    cmd = f'{python_binary} {project_dir}deploy.py start'

    with open(systemd_conf_filepath, 'w') as f:
        f.write(systemd_template.replace('{Description}', app_name).replace('{ConditionPathExists}', python_binary)
                .replace('{PIDFile}', pid_file).replace('{ExecStart}', cmd))
    os.chmod(systemd_conf_filepath, mode=0o755)

    ret = subprocess.run(f'systemctl daemon-reload && systemctl enable {app_name}.gunicorn.service', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ret.returncode != 0:
        print_err(ret.stderr.decode())
        print_err('设置开机自启动失败')
        raise SystemExit
    print_succ(ret.stdout.decode())
    print_succ(ret.stderr.decode())  # warning message
    print_succ('已设置开机自启动')



def start_gunicorn(project_dir, log_dir, app_name):
    """
    调用前先在project目录下创建venv环境,如:
    /root/.pyenv/versions/3.7.2/bin/python -m venv venv
    
    gunicorn >= 20.1.0
    在conf文件中配置wsgi_app
    根据app_name加载相应的配置文件
    """
    cmd = f'{project_dir}venv/bin/gunicorn -c {project_dir}gunicorn_{app_name}_conf.py'
    # 判断是否已启动
    succ, err = exec_shell("pgrep -f '{}'".format(cmd))
    if succ:
        print_err('当前已启动！请通过reload命令重启')
        return

    install_modules(project_dir)

    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ret.returncode != 0:  # 执行失败
        print_err(ret.stderr.decode())
        raise SystemExit

    time.sleep(1)
    read_last_log(log_dir, 6)

    # 配置开机启动
    autostart_at_boot(project_dir, log_dir, app_name)


def reload_gunicorn(project_dir, log_dir):
    install_modules(project_dir)

    pid_file = f'{log_dir}pid.pid'
    pid = read_file(pid_file).strip()
    if not pid:
        print_err(f'重启gunicorn失败,pid不存在:{pid_file}')
    exec_shell('kill -HUP {}'.format(pid))
    time.sleep(1)
    succ, err = read_last_log(log_dir, 30)
    if not succ:
        print_err('重启失败！重启失败！重启失败！')
        return

    # 判断时间是不是3s内
    lines = filter(lambda x: 'Hang up: Master' in x, succ.split('\n'))
    if not lines:
        print_err('重启失败！重启失败！重启失败！')
        return

    for line in lines:
        if datetime.strptime(line[0:19], '%Y-%m-%d %H:%M:%S') > (datetime.now() - timedelta(seconds=3)):
            print_succ('重启成功:{}'.format(line[0:19]))
            return

    print_err('重启失败！重启失败！重启失败！')

