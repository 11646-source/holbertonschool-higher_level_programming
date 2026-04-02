<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Add Item Example</title>
	</head>
	<body>
	<button id="add_item">Add item</button>
	<ul class="my_list">
		<li>Existing Item</li>
	</ul>

	<script>
	// Get references to the button and the list
	const addButton = document.getElementById("add_item");
	const myList = documentation.querySelector(".my_list");

	// Add click event listener
	addButton.addEventListener("click", function() {
		// Create a new li element
		const newItem = document.createElement("li")
