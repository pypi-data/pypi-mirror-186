class Digit2Chinese:
    def __init__(self, digit, style=2):
        """
        :param digit:
        :param style: 1简写 2大写
        """
        self.digit = digit
        self.style = style

    def _digit2chinese_4th(self, digit):
        """
        :param digit: 万以内的处理
        :return:
        """
        # 单零
        if digit == 0:
            return '零'

        if self.style == 1:
            digit_mapping = {
                '0': '零',
                '1': '一',
                '2': '二',
                '3': '三',
                '4': '四',
                '5': '五',
                '6': '六',
                '7': '七',
                '8': '八',
                '9': '九',
            }
            unit = ['', '十', '百', '千', ]
        else:
            digit_mapping = {
                '0': '零',
                '1': '壹',
                '2': '贰',
                '3': '叁',
                '4': '肆',
                '5': '伍',
                '6': '陆',
                '7': '柒',
                '8': '捌',
                '9': '玖',
            }
            unit = ['', '拾', '佰', '仟', ]

        digit_str = str(digit)
        chinese = ''

        # 验证
        if len(digit_str) > 4:
            return digit

        # 反向处理
        for index, digit_c in enumerate(digit_str):
            # 处理 0->零
            if digit_c == '0':
                line = '零'
                chinese += line
                continue

            # 处理非0 5->五/百五/千五
            chinese_c = digit_mapping[digit_c]
            unit_c = unit[index]
            line = chinese_c + unit_c
            line = line[::-1]

            chinese += line

        # 处理多零
        chinese = chinese.replace('零零零', '零').replace('零零', '零')

        # 处理未零
        if chinese[0] == '零':
            chinese = chinese[1:]

        chinese = chinese[::-1]
        return chinese

    def digit2chinese(self):
        # 单零处理
        if self.digit == 0:
            return '零'

        unit = ['', '万', ]
        chinese = ''
        digit_str = str(self.digit)

        # 8位以外是亿 使用递归计算
        chinese_left = ''
        digit_long = len(digit_str)
        middle = ''
        if digit_long > 8:
            digit_str_left = int(digit_str[:-8])
            digit_str_right = digit_str[-8:]
            while True:
                if digit_str_right[0] == '0':
                    middle = '零'
                elif digit_str_right == '0':
                    break
                else:
                    break
                digit_str_right = digit_str_right[1:]
            digit_str_right = int(digit_str_right)

            # 计算左边
            chinese_left = Digit2Chinese(digit_str_left, style=self.style).digit2chinese()
            chinese_left += '亿'

            # 计算右边
            digit_str = str(digit_str_right)

        count = 0
        part = ''
        part_index = 0
        for digit_c in digit_str[::-1]:
            part += digit_c
            count += 1
            if count == 4:
                chinese_part = self._digit2chinese_4th(part)
                chinese_part += unit[part_index]
                chinese = chinese_part + chinese

                # 重新记录片段
                count = 0
                part = ''
                part_index += 1

        # 处理剩下的片段
        if count > 0:
            chinese_part = self._digit2chinese_4th(part)
            chinese_part += unit[part_index]
            chinese = chinese_part + chinese

        # 左右合并
        if chinese_left:
            chinese = f'{chinese_left}{middle}{chinese}'

        # 处理一十
        if chinese.startswith('一十'):
            chinese = chinese[1:]
        return chinese


def digit2chinese(digit, style=2):
    """
    如果发现bug请用电子邮件发送反馈到yanchengxin@yeah.net 谢谢
    我会在第一时间修复.

    :param digit:
    :param style: 1-简写(一/二/三...) 2-大写(壹/贰/叁...)
    :return:
    """
    try:
        digit = int(digit)
    except ValueError as e:
        raise ValueError("只能处理数字") from e

    if digit < 0:
        raise ValueError("只能处理正数")

    digit_obj = Digit2Chinese(digit, style, )
    chinese = digit_obj.digit2chinese()
    return chinese
