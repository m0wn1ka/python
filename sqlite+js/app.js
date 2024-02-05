document.addEventListener("DOMContentLoaded", () => {
  // Create or open the SQLite database
  const db = new SQLite("todo-list.db");

  // Create the "tasks" table if it doesn't exist
  db.query(`
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      description TEXT,
      completed INTEGER DEFAULT 0
    )
  `);

  // Load tasks from the database on page load
  loadTasks();

  // Function to add a new task
  window.addTask = function () {
    const taskInput = document.getElementById("taskInput");
    const description = taskInput.value.trim();

    if (description !== "") {
      // Insert the task into the database
      db.query("INSERT INTO tasks (description) VALUES (?)", [description]);

      // Clear the input field
      taskInput.value = "";

      // Reload the tasks
      loadTasks();
    }
  };

  // Function to load tasks from the database
  function loadTasks() {
    const taskList = document.getElementById("taskList");

    // Clear the task list
    taskList.innerHTML = "";

    // Retrieve tasks from the database
    const tasks = db.query("SELECT * FROM tasks");

    // Display each task in the list
    tasks.forEach((task) => {
      const listItem = document.createElement("li");
      listItem.innerHTML = `
        <span>${task.description}</span>
        <button onclick="deleteTask(${task.id})">Delete</button>
      `;
      taskList.appendChild(listItem);
    });
  }

  // Function to delete a task
  window.deleteTask = function (taskId) {
    // Delete the task from the database
    db.query("DELETE FROM tasks WHERE id = ?", [taskId]);

    // Reload the tasks
    loadTasks();
  };

  // SQLite wrapper for easier database operations
  function SQLite(databaseName) {
    this.db = openDatabase(databaseName, "1.0", "Todo List Database", 5 * 1024 * 1024);
    this.query = function (sql, params, callback) {
      this.db.transaction(function (tx) {
        tx.executeSql(sql, params || [], function (tx, result) {
          if (callback) callback(result.rows);
        });
      });
    };
  }
});
