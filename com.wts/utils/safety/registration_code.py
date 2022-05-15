"""
注册码生成和解码工具
"""
import base64
from datetime import datetime


class RegisterInformation:
    """
    注册信息实体类
    """

    @classmethod
    def register_information(cls):
        """
        无参构造函数
        :return:
        """
        return cls(None, None, None, None, None)

    def __init__(self,
                 validity_period,
                 register_name,
                 contact_email,
                 contact_phone,
                 register_type):
        """
        主构造方法
        :param validity_period: 有效期
        :param register_name: 注册人/单位
        :param contact_email: 联系邮箱
        :param contact_phone: 联系电话
        :param register_type: 注册类型 1=试用验证码，2=正式验证码
        """
        self._validity_period = validity_period
        self._register_name = register_name
        self._contact_email = contact_email
        self._contact_phone = contact_phone
        self._register_type = register_type
        self._register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return '注册时间：{}，有效期：{}，注册人：{}，联系邮箱：{}，联系电话：{}，注册类型：{}' \
            .format(self._register_date,
                    self._validity_period, self._register_name,
                    self._contact_email,
                    self._contact_phone, self._register_type)

    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        self._validity_period = validity_period

    @validity_period.getter
    def validity_period(self):
        return self._validity_period

    @property
    def register_name(self):
        return self._register_name

    @register_name.setter
    def register_name(self, register_name):
        self._register_name = register_name

    @register_name.getter
    def register_name(self):
        return self._register_name

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        self._contact_email = contact_email

    @contact_email.getter
    def contact_email(self):
        return self._contact_email

    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        self._contact_phone = contact_phone

    @contact_phone.getter
    def contact_phone(self):
        return self._contact_phone

    @property
    def register_type(self):
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        self._register_type = register_type

    @register_type.getter
    def register_type(self):
        return self._register_type

    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        self._register_date = register_date

    @register_date.getter
    def register_date(self):
        return self._register_date


class RegisterCodeUtil:
    """
    注册码生成和注册码解码工具类
    """

    @staticmethod
    def generate_register_code(info):
        plaintext = '{}#{}#{}#{}#{}#{}'.format(RegisterCodeUtil.__encode_str(info.register_date),
                                               RegisterCodeUtil.__encode_str(info.validity_period),
                                               RegisterCodeUtil.__encode_str(info.register_name),
                                               RegisterCodeUtil.__encode_str(info.contact_email),
                                               RegisterCodeUtil.__encode_str(info.contact_phone),
                                               RegisterCodeUtil.__encode_str(info.register_type))
        return RegisterCodeUtil.__encode_str(plaintext)

    @staticmethod
    def verify_expired(register_code):
        """
        验证注册码是否过期
        :param register_code: 注册码
        :return: 过期标记：True=已过期，False=未过期
        """
        __register_info = RegisterCodeUtil.get_register_information(register_code)
        # todo 处理注册码状态处理
        return __register_info

    @staticmethod
    def get_register_information(register_code):
        """
        获取注册时间 + 其他注册信息
        :param register_code: 注册码
        :return: 注册日期和注册信息
        """
        encode_str = RegisterCodeUtil.__decode_str(register_code)
        _register_info = RegisterInformation.register_information()
        val_list = encode_str.split('#')
        for idx in range(0, len(val_list)):
            val = RegisterCodeUtil.__decode_str(val_list[idx])
            if idx == 0:
                _register_info.register_date = val
            elif idx == 1:
                _register_info.validity_period = val
            elif idx == 2:
                _register_info.register_name = val
            elif idx == 3:
                _register_info.contact_email = val
            elif idx == 4:
                _register_info.contact_phone = val
            else:
                _register_info.register_type = val
        return _register_info

    @staticmethod
    def __encode_str(plaintext):
        """
        注册信息编码
        :param plaintext: 待编码的明文信息
        :return: 已编码的密文
        """
        return str(base64.b64encode(str(plaintext).encode('utf-8')), 'utf-8')

    @staticmethod
    def __decode_str(plaintext):
        """
        注册码解码
        :param plaintext: 待解码的密文
        :return: 已解码的明文
        """
        return str(base64.b64decode(str(plaintext)), 'utf-8')


if __name__ == '__main__':
    _information = RegisterInformation('2022-05-16', '无名', '12345678@qq.com', '12345478798', 1)

    _code = RegisterCodeUtil.generate_register_code(_information)
    print('注册码：%s' % _code)

    _expired = RegisterCodeUtil.verify_expired(_code)
    print('验证码是否过期：%s' % _expired)

    _info = RegisterCodeUtil.get_register_information(_code)
    print('注册信息：%s' % _info)
