from enum import Enum, unique


@unique
class ApiUrl(str, Enum):
    ''' Raysync interface list '''
    create_task = '/create-task'
    get_task_status = '/get-task-status'
    get_task_list_status = '/get-task-list'
    start_task = '/start-task'
    check_raysync_http = '/check-raysync-http'
    set_transfer_speed = '/set-transmission-parameters'
