在Pygame中，原点(0, 0)位于屏幕左上角

主文件alien_invasion.py创建一系列整个游戏都要用到的对象：
存储在ai_settings中的设置、存储在screen中的主显示surface以及一个飞船实例。
文件alien_invasion.py还包含游戏的主循环，这是一个调用check_events()、ship.update()和update_screen()的while循环