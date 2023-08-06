import mimetypes
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def _get_attach_msg(file_path):  #
    ctype, encoding = mimetypes.guess_type(file_path)  #
    if ctype is None or encoding is not None:  #
        ctype = 'application/octet-stream'  #
    maintype, subtype = ctype.split('/', 1)  #
    with open(file_path, 'rb') as fp:  #
        msg = MIMEBase(maintype, subtype)  #
        msg.set_payload(fp.read())  #
    encoders.encode_base64(msg)  #
    msg.add_header('Content-Disposition', 'attachment', filename=file_path.split('/')[-1])  #
    return msg


def send_mail(task_type, date, from_user_name, from_user, host, port, user,
              passwd, receivers, html_message, log_file=None):
    # 全局变量
    mail_subject = f'[{date}]UFS-{task_type}Azure Events数据更新预警-[{html_message}]'
    # 构建正文信息
    message = f""" <h1> {mail_subject} </h1><hr /><br>
                    UFS Azure Databricks环境下，tracking.events更新出现小时数据为空的情况，信息如下：<br>
                    {html_message}
                  """

    # 构建邮件附件
    msg = MIMEMultipart()  #`
    msg['From'] = formataddr((from_user_name, from_user))  #
    msg['Subject'] = Header(mail_subject, 'utf-8').encode()  #
    msg.attach(MIMEText(message, 'html', 'utf-8'))  #
    if log_file is not None:
        msg.attach(_get_attach_msg(log_file))  # 添加log附件
    # 发送邮件
    smtp = smtplib.SMTP_SSL(host, port)  # 注意这里使用SSL方式，下面的端口使用的是 465
    smtp.ehlo()
    smtp.login(user, passwd)  #
    smtp.sendmail(from_user, receivers, msg.as_string())  #
