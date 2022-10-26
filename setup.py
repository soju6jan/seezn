setting = {
    'filepath' : __file__,
    'use_db': True,
    'use_default_setting': True,
    'home_module': 'program',
    'menu': {
        'uri': __package__,
        'name': '시즌',
        'list': [
            {
                'uri': 'program',
                'name': '프로그램별',
                'list': [
                    {'uri': 'setting', 'name': '설정'},
                    {'uri': 'select', 'name': '선택'},
                    {'uri': 'queue', 'name': '큐'},
                    {'uri': 'list', 'name': '목록'},
                ]
            },
        ]
    },
    'default_route': 'normal',
}
from plugin import *

DEFINE_DEV = False

P = create_plugin_instance(setting)
try:
    if DEFINE_DEV:
        from .mod_program import ModuleProgram
    else:
        from support import SupportSC
        ModuleProgram = SupportSC.load_module_P(P, 'mod_program').ModuleProgram
    
    P.set_module_list([ModuleProgram])
except Exception as e:
    P.logger.error(f'Exception:{str(e)}')
    P.logger.error(traceback.format_exc())
