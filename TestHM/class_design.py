class phone:
    __is_5g_enable = True
    def __check_5g_enable(self):
        if self.__is_5g_enable is True:
            return "5G开启"
        else:
            return "5G关闭 使用4G网络"

    def call_by_5g(self):
        print(self.__check_5g_enable())
        print(f'正在通话中')

    def take_photo(self):
        print("咔哧")

    def power_on(self):
        print("铛铛铛铛")

    def power_off(self):
        print("Bye")

class phone2022(phone):
    face_id = True

    def call_by_5g_face(self):
        print(f'新升级5g 正在通话中 {self.face_id}')


phone = phone2022()
phone.call_by_5g()
phone.call_by_5g_face()









