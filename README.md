# 0x00. AirBnB clone - The console
## description of the project : 

I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

+ After 4 months, you will have a complete web application composed by:

	- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
	- A website (the front-end) that shows the final product to everybody: static and dynamic
	- A database or files that store data (data = objects)
	- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![Screenshot of The console will be a tool to validate this storage engine.](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png)

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240209%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240209T204020Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=126830d6a3f0c93e37f34d7a1b32b1947278a6fe84bf3c54d632d6bdcd0a16cc" alt="" loading="lazy" style=""></p>

## The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
