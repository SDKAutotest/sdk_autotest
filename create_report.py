import time

def create_rep(result):
	print("----传入的测试结果：",result)
	if result["case_code"]:
		pass_or_fail = "测试通过"
	else:
		pass_or_fail = "测试未通过"
	demo = """
	<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>网盟SDK自动化测试报告</title>
    <style>
        /*上部分样式*/
        div#report_head{
            position: absolute;
            top:0px;
            height: 10%;
            width: 100%;
        }
        /*标题样式*/
        h1#report_head_title{
            padding: 0px;
            margin: 0px;
            position: absolute;
            left: 25%;
            width:50%;
            top: 20%;
            height: 60%;
        }
        /*数据部分样式*/
        div#report_body{
            position: absolute;
            top:10%;
            width: 100%;
            
        }
        table{
            width: 100%;
            line-height: 30px;
        }
        .event_des_number{
            width:10%;
        }
        .event_des{
            width: 9%;
        }
    </style>
</head>"""+"""
<body style="background-color:#7CFC00;">
    <!-- 报告的头部 -->
    <div id="report_head">
        <h1 id="report_head_title">%s</h1>
    </div>
    <!-- 报告的主体部分 -->
    <div id="report_body">
        <table id="report_body_table" border="1">
            <!--假设10个事件,11列-->
            <!--测试结果，表头-->
            <thead>
                <tr align="left">
                    <th colspan="5">测试结论 : %s</th>
                    <th colspan="6">测试时间 : %s</th>
                </tr>
            </thead>
            <!--埋点测试结果，数据-->
            <tbody>
                <tr align="left">
                    <td class="event_des_number"></td>
                    <td class="event_des">点击事件<br>
                        label = click<br>
                        tag = splash_ad<br>
                        tag = splash_ad<br>
                        tag = splash_ad<br>
                        tag = splash_ad<br>
                        xxxxx……
                    </td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                    <td class="event_des">事件</td>
                </tr>
                <tr align="center">
                    <td class="event_des_number">预期数量</td>
                    <td class="event_des">5</td>
                    <td class="event_des">4</td>
                    <td class="event_des">3</td>
                    <td class="event_des">2</td>
                    <td class="event_des">1</td>
                    <td class="event_des">0</td>
                    <td class="event_des">6</td>
                    <td class="event_des">7</td>
                    <td class="event_des">8</td>
                    <td class="event_des">9</td>
                </tr>
                <tr align="center">
                    <td class="event_des_number">实际数量</td>
                    <td class="event_des">5</td>
                    <td class="event_des">4</td>
                    <td class="event_des">3</td>
                    <td class="event_des">2</td>
                    <td class="event_des">1</td>
                    <td class="event_des">0</td>
                    <td class="event_des">6</td>
                    <td class="event_des">7</td>
                    <td class="event_des">8</td>
                    <td class="event_des">9</td>
                </tr>
                <tr align="center">
                    <td class="event_des_number">结果差值</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                    <td class="event_des">0</td>
                </tr>
            </tbody>
            <!--功能测试，记录产生的错误-->
            <tfoot>
                <tr>
                    <td colspan="11">测试中出现的功能缺陷及异常</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td colspan="10">开屏无跳过按钮</td>
                </tr>
            </tfoot>
        </table>
    </div>
</body>
</html>
	"""%(result["title"],pass_or_fail,result["run_time"])
	with open("./report/%s"%result["run_time"],"w",encoding = "utf-8") as f:
		f.write(demo)










