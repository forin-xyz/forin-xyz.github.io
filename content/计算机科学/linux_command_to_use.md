Title: Linux 常用命令摘要


    tar -czvf xx.gz.tar $directory  # 压缩打包



    mongodump -h $DB_SERVER -d $DB_NAME -o $AIM_DIR # mongodb 备份



    ln -s $SOURCE_FILE $SOFT_LINK # 软连接， $SOURCE_FILE 就是源文件，$SOFT_LINK是链接文件名,其作用相当于$SOFT_LINK是$SOURCE_FILE的别名, 与windows中的快捷方式作用相似




    ps aux | grep -v grep   # 显示出所有的进程，去处掉当前的grep进程, 以用户为主的格式来显示程序状况, 且不以终端机为区分

    ps ef | grep -v grep    # 显示出所有的进程，去处掉当前的grep进程, 用ASCII字符显示树状结构，表达程序间的相互关系
