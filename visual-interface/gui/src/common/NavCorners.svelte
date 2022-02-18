<script>
	// Imports
	import { Link } from "svelte-routing";

</script>

<nav>
	<Link to="/"><img src="graphics/homepage.svg" alt="Home" width="32px" /></Link>
	<Link to="mode"><img src="graphics/back.svg" alt="Back" width="32px" /></Link> <!--TODO: add conditions -->
	<img src="graphics/battery-status-full.svg" alt="Battery Status" width="32px" class="battery-status" /> <!--TODO: add dynamic battery status -->
</nav>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>