# Enterprise Verification Report

Date: 2026-01-21 12:01:31

## 1. Python Version
- Command: `C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\.venv\Scripts\python.exe --version`
- Output: `Python 3.11.9`
- Result: PASS

## 2. Pip Version
- Command: `pip --version`
- Output: `pip 25.3 from C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\.venv\Lib\site-packages\pip (python 3.11)`
- Result: PASS

## 3. Node/NPM Version
- Node Output: `v20.11.0`
- NPM Output: `10.2.4`
- Result: PASS

## 4. Dependencies Installation
- Output: `0.0,>=3.7.1->fastapi==0.104.1->-r C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\server\requirements.txt (line 2)) (1.3.1)
Requirement already satisfied: six>=1.5 in c:\users\ga.castillo\onedrive - motta internacional, s.a\escritorio\control de inventrio\.venv\lib\site-packages (from python-dateutil>=2.8.2->pandas==2.1.3->-r C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\server\requirements.txt (line 7)) (1.17.0)` ...
- Result: PASS

## 5. Automated Tests
- Output: `=================================== ERRORS ====================================
______________ ERROR collecting tests/test_email_notification.py ______________
ImportError while importing test module 'C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\tests\test_email_notification.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\..\AppData\Local\Python\pythoncore-3.11-64\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\test_email_notification.py:10: in <module>
    from email_notifier import send_notification_email, load_email_config
E   ModuleNotFoundError: No module named 'email_notifier'
____________________ ERROR collecting tests/test_filter.py ____________________
ImportError while importing test module 'C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\tests\test_filter.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\..\AppData\Local\Python\pythoncore-3.11-64\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\test_filter.py:5: in <module>
    from server.main import leer_excel, SHEET_NAME_GENERAL
E   ImportError: cannot import name 'leer_excel' from 'server.main' (C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\server\main.py)
____________________ ERROR collecting tests/test_simple.py ____________________
.venv\Lib\site-packages\_pytest\runner.py:341: in from_call
    result: Optional[TResult] = func()
        cls        = <class '_pytest.runner.CallInfo'>
        duration   = 2.118919400003506
        excinfo    = <ExceptionInfo KeyError('metricas') tblen=15>
        func       = <function pytest_make_collect_report.<locals>.<lambda> at 0x000002614847B100>
        precise_start = 86828.0767527
        precise_stop = 86830.1956721
        reraise    = None
        result     = None
        start      = 1769014912.2579355
        stop       = 1769014914.3689797
        when       = 'collect'
.venv\Lib\site-packages\_pytest\runner.py:372: in <lambda>
    call = CallInfo.from_call(lambda: list(collector.collect()), "collect")
        collector  = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\python.py:531: in collect
    self._inject_setup_module_fixture()
        __class__  = <class '_pytest.python.Module'>
        self       = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\python.py:545: in _inject_setup_module_fixture
    self.obj, ("setUpModule", "setup_module")
        has_nose   = True
        self       = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\python.py:310: in obj
    self._obj = obj = self._getobj()
        obj        = None
        self       = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\python.py:528: in _getobj
    return self._importtestmodule()
        self       = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
        importmode = 'prepend'
        self       = <Module tests/test_simple.py>
.venv\Lib\site-packages\_pytest\pathlib.py:567: in import_path
    importlib.import_module(module_name)
        mode       = <ImportMode.prepend: 'prepend'>
        module_name = 'test_simple'
        p          = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests/test_simple.py')
        path       = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests/test_simple.py')
        pkg_path   = None
        pkg_root   = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests')
        root       = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO')
..\..\..\AppData\Local\Python\pythoncore-3.11-64\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
        level      = 0
        name       = 'test_simple'
        package    = None
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
        level      = 0
        name       = 'test_simple'
        package    = None
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
        import_    = <function _gcd_import at 0x000002612A4E3D80>
        module     = <object object at 0x000002612A514050>
        name       = 'test_simple'
<frozen importlib._bootstrap>:1147: in _find_and_load_unlocked
    ???
        import_    = <function _gcd_import at 0x000002612A4E3D80>
        name       = 'test_simple'
        parent     = ''
        parent_spec = None
        path       = None
        spec       = ModuleSpec(name='test_simple', loader=<_pytest.assertion.rewrite.AssertionRewritingHook object at 0x000002612C1AC910>,...'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py')
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
        module     = <module 'test_simple' from 'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py'>
        spec       = ModuleSpec(name='test_simple', loader=<_pytest.assertion.rewrite.AssertionRewritingHook object at 0x000002612C1AC910>,...'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py')
.venv\Lib\site-packages\_pytest\assertion\rewrite.py:186: in exec_module
    exec(co, module.__dict__)
        cache_dir  = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests/__pycache__')
        cache_name = 'test_simple.cpython-311-pytest-7.4.3.pyc'
        co         = <code object <module> at 0x000002612BFC7A40, file "C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\tests\test_simple.py", line 1>
        fn         = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests/test_simple.py')
        module     = <module 'test_simple' from 'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py'>
        ok         = True
        pyc        = WindowsPath('C:/Users/ga.castillo/OneDrive - Motta Internacional, S.A/Escritorio/CONTROL DE INVENTRIO/tests/__pycache__/test_simple.cpython-311-pytest-7.4.3.pyc')
        self       = <_pytest.assertion.rewrite.AssertionRewritingHook object at 0x000002612C1AC910>
        source_stat = os.stat_result(st_mode=33206, st_ino=4222124651229038, st_dev=1382144472, st_nlink=1, st_uid=0, st_gid=0, st_size=798, st_atime=1769006045, st_mtime=1768929228, st_ctime=1768929228)
        state      = <_pytest.assertion.AssertionState object at 0x000002612C1AEBD0>
        write      = True
tests\test_simple.py:15: in <module>
    print(f"Total ubicaciones: {data['metricas']['total_productos']}")
E   KeyError: 'metricas'
        __builtins__ = <builtins>
        __cached__ = 'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\__pycache__\\test_simple.cpython-311.pyc'
        __doc__    = None
        __file__   = 'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py'
        __loader__ = <_pytest.assertion.rewrite.AssertionRewritingHook object at 0x000002612C1AC910>
        __name__   = 'test_simple'
        __package__ = ''
        __spec__   = ModuleSpec(name='test_simple', loader=<_pytest.assertion.rewrite.AssertionRewritingHook object at 0x000002612C1AC910>,...'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\tests\\test_simple.py')
        data       = {'data': {'datos_categoria': [{'con_discrepancia': 0, 'exactitud': 100.0, 'nombre': 'CANNING LATINOAMERICA', 'total_ub...d9e54db-8c90-4ac4-a2f6-08d634fc1f9c', 'timestamp': '2026-01-21T17:01:54.368979Z', 'version': '2.0.0'}, 'success': True}
        requests   = <module 'requests' from 'C:\\Users\\ga.castillo\\OneDrive - Motta Internacional, S.A\\Escritorio\\CONTROL DE INVENTRIO\\.venv\\Lib\\site-packages\\requests\\__init__.py'>
        response   = <Response [200]>
        url        = 'http://localhost:8001/api/dashboard/completo'
------------------------------- Captured stdout -------------------------------
Testing parameter reception...
============================================================

[TEST 1] Single cliente parameter:
URL: http://localhost:8001/api/dashboard/completo?cliente=CANNING+LATINOAMERICA
============================== warnings summary ===============================
.venv\Lib\site-packages\pydantic\_internal\_config.py:268
.venv\Lib\site-packages\pydantic\_internal\_config.py:268
  C:\Users\ga.castillo\OneDrive - Motta Internacional, S.A\Escritorio\CONTROL DE INVENTRIO\.venv\Lib\site-packages\pydantic\_internal\_config.py:268: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.5/migration/
    warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR tests/test_email_notification.py
ERROR tests/test_filter.py
ERROR tests/test_simple.py - KeyError: 'metricas'
!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!
2 warnings, 3 errors in 11.66s`
- Result: FAIL

## 6. API Healthy Endpoints
- Endpoint: `http://localhost:8000/health`
  - Output: `HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /health (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8000): Failed to establish a new connection: [WinError 10061] No se puede establecer una conexión ya que el equipo de destino denegó expresamente dicha conexión"))`
  - Result: FAIL

- Endpoint: `http://localhost:8000/health/ready`
  - Output: `HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /health/ready (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8000): Failed to establish a new connection: [WinError 10061] No se puede establecer una conexión ya que el equipo de destino denegó expresamente dicha conexión"))`
  - Result: FAIL

- Endpoint: `http://localhost:8000/api/system/metrics`
  - Output: `HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /api/system/metrics (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8000): Failed to establish a new connection: [WinError 10061] No se puede establecer una conexión ya que el equipo de destino denegó expresamente dicha conexión"))`
  - Result: FAIL

- Endpoint: `http://localhost:8000/api/system/version`
  - Output: `HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /api/system/version (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8000): Failed to establish a new connection: [WinError 10061] No se puede establecer una conexión ya que el equipo de destino denegó expresamente dicha conexión"))`
  - Result: FAIL
