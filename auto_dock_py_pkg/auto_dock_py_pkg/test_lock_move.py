key_lock_enter = 0

while(1):
    if key_lock_enter == 0 :
        key_enter = input('press "Enter" to start move')
        print(key_enter)
    if key_enter != "1234567890-=qwertyuiop[asdfghzxcvbnm,.jk":
        key_lock_enter = 1
        print(1)