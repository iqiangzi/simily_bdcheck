;first make sure the number of arguments passed into the scripts is more than 1
;If $CmdLine[0]<2 Then Exit EndIf ;if parmas num <2 ,then break
;$CmdLine[0] ;参数的数量
;$CmdLine[1] ;第一个参数 (脚本名称后面)
;$CmdLine[2] ;第二个参数
;都是从cmd传入参数
handleUpload($CmdLine[1],$CmdLine[2])

;定义上传函数，有两个参数，第一个是浏览器名字，第二参数是文件路径
 Func handleUpload($browser, $uploadfile)
     Dim $title                          ;定义一个title变量
            ;根据弹窗的title来判断是什么浏览器
            If $browser="ie" Then                          ; 代表FIREFOX浏览器
                  $title="[CLASS:#32770]"
            ElseIf $browser="chrome" Then               ; 代表谷歌浏览器
                 $title="[CLASS:#32770]"
            ElseIf    $browser="firefox" Then             ; 代表火狐浏览器
                  $title="[CLASS:#32770]"
			EndIf

			;ControlFocus("[CLASS:#32770]", "","Edit1")
            if WinWait("[CLASS:#32770]","",200) Then ;等待弹出出现，最大等待时间是2min
				WinActivate($title)
				;找到弹出窗口之后，激活当前窗口
				Sleep(2000)
				ControlCommand($title,"","ComboBox2","SelectString","所有文件")
				Sleep(2000)
				ControlSetText($title,"","Edit1",$uploadfile)  ;把文件路径放入输入框，此”Edit1“是用FinderTool获取到的
				Sleep(2000)
				;click on  the open button
				ControlClick("[CLASS:#32770]", "打开","Button1")  ;点击保存或者打开或者上传按钮，此“Button1”使用FinderTool获取到的
				Sleep(1000)
            Else
            Return False
            EndIf
 EndFunc