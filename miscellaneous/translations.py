english_to_chinese = {
	"Last name": "名字",
	"First name": "姓",
	"Chinese name": "中文名字",
	"School": "学校位置",
	"Barcode": "条码号",
	"Date of birth": "生日",
	"Age": "年龄",
	"Gender": "性别",
	"Home phone": "家庭电话",
	"Cell phone": "手机",
	"Cell phone 2": "手机 2",
	"Address": "住址",
	"State": "州",
	"City": "城市",
	"Zipcode": "邮政编码",
	"E-mail": "电子邮件",
	"Date": "日期",
	"Time": "Time",
	"Check-in time": "到达时间",
	"Check-out time": "离开时间",
	"Start time": "工作开始",
	"Start date": "Start date",
	"End date": "End date",
	"Notes": "笔记",
	"Teacher was not found! Please try again": "找不到的学生！ 键入正确的名称或与系统管理员联系",
	"Are you sure you would like to add this teacher?": "你确定你想这位老师向数据库中添加?",
	"Teacher with this barcode already exists. Adding this teacher will overwrite the existing teacher. Would you like to overwrite?": "一个老师用相同的条码。如果想添加这个老师,你要覆盖旧的老师",
	"Teacher has been added to the database": "教师已被添加到数据库中",
	"Check in the teacher?": "入住这个老师",
	"Check out the teacher?": "签出这个教师",
	"Teacher checked-out today. Overwrite check-out?": "改写签出",
	"Teacher checked-in today. Overwrite check-in?": "改写入住",
	"Teacher has not checked-in today": "Teacher has not checked-in today",
	"Ok": "确认",
	"Yes": "确认",
	"No": "拒绝",
	"Export database": "数据报告",
	"Import data": "输入文档",
	"Import time data": "输入时间文档",
	"Import/export": "导入数据库/数据报告",
	"Current database file": "当前数据库文件",
	"Browse": "浏览",
	"File Path": "File Path",
	"Back": "返回",
	"Next": "下一次",
	"Save": "保存",
	"Change database": "选择数据库",
	"Add teacher": "新增教师",
	"Check-in teacher": "登錄教师",
	"Check-out teacher": "註銷教师",
	"Teacher database": "老师资料库",
	"Back to main menu": "返回主界面",
	"Exit": "关闭软件",
	"Search": "搜索老师",
	"Search By": "搜索方式",
	"Save Teacher": "储存老师数据库",
	"Cancel": "取消",
	"Return to main window?": "返回主窗口而不保存",
	"Close": "关闭",
	"Previous": "上一页",
	"Last page": "最后一页",
	"Import succesful": "导入成功",
	"General": "教师信息",
	"Contact": "联络",
	"Card printed": "已打印卡",
	"Phone number": "电话号码",
	"RYB teacher management" : "红黄蓝老师管理软件",
	"Print report": "每日报告",
	"Salary report": "创造工资",
	"Today's date": "今天日期",
	"Last payment": "上次支付",
	"Dollar/hour": "时薪",
	"Confirm time": "确认时间",
	"Confirm": "Confirm",
	"Yes, enter time": "输入工作起始时间",
	"Brooklyn": "布鲁克林学校",
	"Chinatown": "唐人街学校",
	"Elmhurst": "艾姆赫斯特学校",
	"Flushing": "法拉盛学校",
	"Choose school": "选择学校",
	"Print successful": "工资做出",
	"Choose PW file": "选择密数据库",
	"New PW file": "New PW file",
	"New database": "创造新数据库",
	"Encrypt database": "转换为加密数据库",
	"Password must be reset. Please enter the old password followed by the new password": "Password must be reset. Please enter the old password followed by the new password",
	"Enter password": "输入密码",
	"Reset DB manager PW": "复位密码",
	"Password has been reset": "Password has been reset",
	"You have entered the wrong password, try again": "You have entered the wrong password, try again",
	"Choose marker file": "选择工资据库",
	"New marker file": "创造工资据库",
	"Database backup successful": "创建数据库成功",
	"Manual entry": "登錄教师!", #get new translation for manual entry
	"School": "School",
	"Invalid date": "Invalid date",
	"Teacher print successful": "教师报告成功",
	"Check-out cannot be earlier than check-in": "不能签出在签入前",
	"Teacher has not checked-in for that date": "老师没有入住在这日期",
	"Cannot check in: entered time is ahead of current time": "不能登记未来时间",
	"Password file": "assword file",
	"Preview": "Preview",
	"Output file": "Output file",
	"Source excel": "Source excel",
	"Invalid file type": "Invalid file type",
	"Print simple report": "Print simple report"
}

chinese_to_english = {value:key for key, value in english_to_chinese.items()}

one_to_one = len(chinese_to_english) == len(english_to_chinese)