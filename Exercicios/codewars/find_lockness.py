def is_lock_ness_monster(string):
    #your code here
    if string.find("three fifty")>-1 or string.find("3.50")>-1 or string.find("tree fiddy")>-1:
        return True
    else:
        return False


print(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"), True)
print(is_lock_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"),True)
print(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"),True)
print(is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."), False)
print(is_lock_ness_monster("I will absolutely, positively, never give that darn Lock Ness Monster any of my three dollars and fifty cents"),False)
print(is_lock_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."),False)
print(is_lock_ness_monster("Hello, I come from the year 3150 to bring you good news!"),False)
print(is_lock_ness_monster("By 'tree fiddy' I mean 'three fifty'"), True)
print(is_lock_ness_monster("I will be at the office by 3:50 or maybe a bit earlier, but definitely not before 3, to discuss with 50 clients"),False)
print(is_lock_ness_monster(""),False)