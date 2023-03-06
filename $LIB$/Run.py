def run(n):
  with open('../$APP$/'+n+'.py') as f:
    try:exec("print('Run '+n);"+f.read(),{'n':n})
    except Exception as e:
        if 'no active exception to reraise'!=str(e):
            with open('../$USR$/Latest_ERR.txt','w') as g:
                g.write(str(e))