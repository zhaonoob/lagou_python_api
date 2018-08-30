import models.recruit as recruit
from flask import Blueprint, jsonify

recruit_blue_print = Blueprint('recruit', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@recruit_blue_print.route('/lists/<page>')
def lists(page):
    return jsonify({'status': status, 'dataList': recruit.get_recruits_list(page)})


@recruit_blue_print.route('/single/<rid>')
def recruit_singe(rid):
    return jsonify({'status': status, 'object': recruit.get_recruits_single(rid)})
