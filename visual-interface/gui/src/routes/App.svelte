<script>
	// Imports
	import { Router, Route } from "svelte-routing";
	import NavCorners from "../common/NavCorners.svelte";
	import Search from "../lib/search/Search.svelte";
	import Monitor from "../lib/monitor/Monitor.svelte";
	import Mode from "./Mode.svelte";
	import Home from "./Home.svelte";

	export let url = ""; // necessary for router
	const basepath = /^\/?[a-zA-Z]+:/.test(window.location.pathname)
    ? window.location.pathname.substr(0, window.location.pathname.indexOf(":") + 1)
    : "/"	// necessary for electron
	console.log(basepath);

	// Props
	export let name;
</script>



<Router url="{url}" basepath={basepath}>
	<NavCorners />
	
	<div>
		<Route path="mode" component="{Mode}" /> 
		<Route path="search" component="{Search}" /> 
		<Route path="monitor" component="{Monitor}" /> 
		<Route path="/" ><Home {name} /></Route>
	</div>
</Router>


<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>