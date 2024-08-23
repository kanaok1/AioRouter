# aiorouter 🚀

**aiorouter** is a convenient library designed to simplify the management of routers in projects based on `aiogram`. It automates the process of collecting all routers in your project, making it easier to organize and scale your bot.

### 📦 Installation

```bash
pip install aiorouter
```
💡 Features
🔍 Automatic Router Discovery: The library recursively scans all directories and modules in your project, finding and gathering all routers in one place.
🚀 Easy to Use: A simple and intuitive API that allows you to quickly set up and use it in your project.
### 🛠️ Example Usage

from aiorouter import RouterManager

Specify the root directory of your project where the router modules are located.
router_manager = RouterManager(root_path="bot")

Collect all routers from the modules.
routers = router_manager.collect_routers()

Now you have a list of all routers, ready to be used in your bot!
for router in routers:
    # Add each router to the main bot application
    app.include_router(router)

### 🌟 Why Choose aiorouter?
📈 Simplifies Development: Focus on your bot's logic without worrying about organizational details.
⏱️ Saves Time: Automatically collecting routers reduces the chances of errors and saves you time.
