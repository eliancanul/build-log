
Today was my first day learning the basics of computer science.
Mostly was a setup and configuration day, but also a day full of deep concepts like what a ssh-agent does, how different programs comunicate with each other using trees of work. 

Different commands for Unix, like what "<, $(), |" does. 

That when a "-" goes after a command is called a flag, and commands also have subcommands like git (command) push (subcommand) -u (flag). 

Local vs Remote github repositories. Actually, almost all the basic functions of git, but clearly I have to use it more often to truthfully memorize what everything does without looking for the command to write it. 

The thing that i'm most proud that I learn today was really how in trying to learn what this command means: 

	eval "$(ssh-agent -s)"

While trying to understand how this command works I was mostly intrigue by how every part of the command; first of all, has an order, which in this case, the first one is a call for the ssh-agent to run, then the flag "-s" specifically formatted for my shell, and then the $ is replaced with the output of what is inside of it. All of this is what the command eval is going to excecute as a command. 

All of that to later know that in mac I just have to use Keychain when using ssh-add. But really helped me a lot to understand a very interesting way of thinking that UNIX/LINUX have since 1970 according to my personal IA, and is that every program is made to complete a single task in a very optimized way, and made with the purpuse of connecting with others. That's something that I love about Linux, it has a really good organization with it's programs. 

