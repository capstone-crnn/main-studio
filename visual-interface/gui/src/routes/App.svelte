<script>
	// Imports
	import Router from "svelte-spa-router";
	import NavCorners from "../common/NavCorners.svelte";
	import Search from "../lib/search/Search.svelte";
	import Monitor from "../lib/monitor/Monitor.svelte";
	import Mode from "./Mode.svelte";
	import Home from "./Home.svelte";

	
	const routes = {
		"/": Home,
		"/mode": Mode,
		"/search": Search,
		"/monitor": Monitor
	}
</script>

<main>
	<NavCorners />
	<Router {routes} />
</main>


<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>