import sys


def l111ll1ll1l1l1llIl1l1(ll11ll1lll1ll11lIl1l1, ll11llll1111111lIl1l1):
    from pathlib import Path
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    import io
    import os

    def l1ll1l1lll111111Il1l1(*ll11l11111lll1llIl1l1):

        for l11llll1l1111l11Il1l1 in ll11l11111lll1llIl1l1:
            os.close(l11llll1l1111l11Il1l1)

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
    else:
        from multiprocessing import semaphore_tracker as tracker 

    llll1l1l1l11l1llIl1l1 = tracker.getfd()
    ll11ll1lll1ll11lIl1l1._fds.append(llll1l1l1l11l1llIl1l1)
    ll11llll1l111l1lIl1l1 = spawn.get_preparation_data(ll11llll1111111lIl1l1._name)
    llllll111ll11ll1Il1l1 = io.BytesIO()
    set_spawning_popen(ll11ll1lll1ll11lIl1l1)

    try:
        reduction.dump(ll11llll1l111l1lIl1l1, llllll111ll11ll1Il1l1)
        reduction.dump(ll11llll1111111lIl1l1, llllll111ll11ll1Il1l1)
    finally:
        set_spawning_popen(None)

    l1l111l11llll111Il1l1ll1lll1l1ll1llllIl1l1ll1l1l1111l1ll1lIl1l1l1l11l1ll111llllIl1l1 = None
    try:
        (l1l111l11llll111Il1l1, ll1lll1l1ll1llllIl1l1, ) = os.pipe()
        (ll1l1l1111l1ll1lIl1l1, l1l11l1ll111llllIl1l1, ) = os.pipe()
        lllll1l111l1111lIl1l1 = spawn.get_command_line(tracker_fd=llll1l1l1l11l1llIl1l1, pipe_handle=ll1l1l1111l1ll1lIl1l1)


        ll111ll11ll1lll1Il1l1 = str(Path(ll11llll1l111l1lIl1l1['sys_argv'][0]).absolute())
        lllll1l111l1111lIl1l1 = [lllll1l111l1111lIl1l1[0], '-B', '-m', 'reloadium', 'spawn_process', str(llll1l1l1l11l1llIl1l1), 
str(ll1l1l1111l1ll1lIl1l1), ll111ll11ll1lll1Il1l1]
        ll11ll1lll1ll11lIl1l1._fds.extend([ll1l1l1111l1ll1lIl1l1, ll1lll1l1ll1llllIl1l1])
        ll11ll1lll1ll11lIl1l1.pid = util.spawnv_passfds(spawn.get_executable(), 
lllll1l111l1111lIl1l1, ll11ll1lll1ll11lIl1l1._fds)
        ll11ll1lll1ll11lIl1l1.sentinel = l1l111l11llll111Il1l1
        with open(l1l11l1ll111llllIl1l1, 'wb', closefd=False) as l11111ll1111111lIl1l1:
            l11111ll1111111lIl1l1.write(llllll111ll11ll1Il1l1.getbuffer())
    finally:
        ll111l1111l1ll11Il1l1 = []
        for l11llll1l1111l11Il1l1 in (l1l111l11llll111Il1l1, l1l11l1ll111llllIl1l1, ):
            if (l11llll1l1111l11Il1l1 is not None):
                ll111l1111l1ll11Il1l1.append(l11llll1l1111l11Il1l1)
        ll11ll1lll1ll11lIl1l1.finalizer = util.Finalize(ll11ll1lll1ll11lIl1l1, l1ll1l1lll111111Il1l1, ll111l1111l1ll11Il1l1)

        for l11llll1l1111l11Il1l1 in (ll1l1l1111l1ll1lIl1l1, ll1lll1l1ll1llllIl1l1, ):
            if (l11llll1l1111l11Il1l1 is not None):
                os.close(l11llll1l1111l11Il1l1)


def __init__(ll11ll1lll1ll11lIl1l1, ll11llll1111111lIl1l1):
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    from multiprocessing.popen_spawn_win32 import TERMINATE, WINEXE, WINSERVICE, WINENV, _path_eq
    from pathlib import Path
    import os
    import msvcrt
    import sys
    import _winapi

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
        from multiprocessing.popen_spawn_win32 import _close_handles
    else:
        from multiprocessing import semaphore_tracker as tracker 
        _close_handles = _winapi.CloseHandle

    ll11llll1l111l1lIl1l1 = spawn.get_preparation_data(ll11llll1111111lIl1l1._name)







    (l11lll11llll1l11Il1l1, l1lll11l11l1l11lIl1l1, ) = _winapi.CreatePipe(None, 0)
    l1ll1l1ll11ll111Il1l1 = msvcrt.open_osfhandle(l1lll11l11l1l11lIl1l1, 0)
    l1ll11l1l11111llIl1l1 = spawn.get_executable()
    ll111ll11ll1lll1Il1l1 = str(Path(ll11llll1l111l1lIl1l1['sys_argv'][0]).absolute())
    lllll1l111l1111lIl1l1 = ' '.join([l1ll11l1l11111llIl1l1, '-B', '-m', 'reloadium', 'spawn_process', str(os.getpid()), 
str(l11lll11llll1l11Il1l1), ll111ll11ll1lll1Il1l1])



    if ((WINENV and _path_eq(l1ll11l1l11111llIl1l1, sys.executable))):
        l1ll11l1l11111llIl1l1 = sys._base_executable
        lll1llllll11l111Il1l1 = os.environ.copy()
        lll1llllll11l111Il1l1['__PYVENV_LAUNCHER__'] = sys.executable
    else:
        lll1llllll11l111Il1l1 = None

    with open(l1ll1l1ll11ll111Il1l1, 'wb', closefd=True) as l1llll1l11ll111lIl1l1:

        try:
            (l11l11l11111l11lIl1l1, lllll1l1l11l1l11Il1l1, l1l11l1l111lll11Il1l1, ll1l111lll1l1l11Il1l1, ) = _winapi.CreateProcess(l1ll11l1l11111llIl1l1, lllll1l111l1111lIl1l1, None, None, False, 0, lll1llllll11l111Il1l1, None, None)


            _winapi.CloseHandle(lllll1l1l11l1l11Il1l1)
        except :
            _winapi.CloseHandle(l11lll11llll1l11Il1l1)
            raise 


        ll11ll1lll1ll11lIl1l1.pid = l1l11l1l111lll11Il1l1
        ll11ll1lll1ll11lIl1l1.returncode = None
        ll11ll1lll1ll11lIl1l1._handle = l11l11l11111l11lIl1l1
        ll11ll1lll1ll11lIl1l1.sentinel = int(l11l11l11111l11lIl1l1)
        if (sys.version_info > (3, 8, )):
            ll11ll1lll1ll11lIl1l1.finalizer = util.Finalize(ll11ll1lll1ll11lIl1l1, _close_handles, (ll11ll1lll1ll11lIl1l1.sentinel, int(l11lll11llll1l11Il1l1), 
))
        else:
            ll11ll1lll1ll11lIl1l1.finalizer = util.Finalize(ll11ll1lll1ll11lIl1l1, _close_handles, (ll11ll1lll1ll11lIl1l1.sentinel, ))



        set_spawning_popen(ll11ll1lll1ll11lIl1l1)
        try:
            reduction.dump(ll11llll1l111l1lIl1l1, l1llll1l11ll111lIl1l1)
            reduction.dump(ll11llll1111111lIl1l1, l1llll1l11ll111lIl1l1)
        finally:
            set_spawning_popen(None)
