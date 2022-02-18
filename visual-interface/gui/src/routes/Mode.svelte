<script>
	// Imports
	import { Link } from "svelte-routing";

</script>

<main>
	<h1> Mode </h1>

	<div>
		<h2>Search & Rescue</h2>
		<p>Use this mode to detect nearby vital signs</p>
		<Link to="search">
			<button>
				<img src="/graphics/human-resources-search-employees.svg" alt="Search" width="64px" /> <!--TODO: Fix images -->
			</button>
		</Link>
	</div>

	<div>
		<h2>Monitor Vitals</h2>
		<p>Calibrate device to measure immediate vital signs</p>
		<Link to="monitor">
			<button>
				<img src="graphics/graph-stats-circle.svg" alt="Monitor" width="64px" /> <!--TODO: Fix images -->
			</button>
		</Link>
	</div>
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
		/* background-color: #1c2541; */
	}

	h1 {
		color: #ff3e00;
		/* color: #a2d729;
		text-shadow:1px 1px 10px #c4e675; */
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>