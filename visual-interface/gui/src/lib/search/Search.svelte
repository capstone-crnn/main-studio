<script>
	// Imports
	import ActionBar from "../../common/ActionBar.svelte";
	
	const actionBarConfig = [
		{
			text: "Play",
			disabled: false,
			action: () => {}
		},
		{
			text: "Stop",
			disabled: false,
			action: () => {}
		},
		{
			text: "Capture",
			disabled: false,
			action: () => {}
		},
		{
			text: "Delete",
			disabled: false,
			action: () => {}
		}
	]
</script>

<main>
	<h1>Search</h1>

	<div>
		<h2>Initiate search</h2>
		<p>Touch the play icon</p>
	</div>

	<div>
		<h3>Last spotted:</h3>
		<p>—</p>
	</div>

	<ActionBar config={actionBarConfig} />

</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>