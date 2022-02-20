<script>
	// Imports
	import { link } from "svelte-spa-router";


	let version;
	const get_version = async () => {
		version = await api.GetVersion();
	}
</script>

<main class="container h-full px-20 mx-auto my-auto text-center">
	<h1 class="py-12 text-3xl">
		finderFly Logo
	</h1>
	<a href="/mode" use:link>
		<button class="p-2 font-sans text-xl hover:bg-orange-300">
			START
		</button>
	</a>
</main>

<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;


</style>