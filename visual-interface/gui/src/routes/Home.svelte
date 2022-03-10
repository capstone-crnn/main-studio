<script>
	// Imports
	import { link } from "svelte-spa-router";

</script>

<main class="container h-full px-20 mx-auto my-auto text-center">

	<div class="pt-12">
		<img src="graphics/GroupS01_Logo-02.svg" alt="Logo" class="inline m-2 align-middle w-28" />
		<h1 class="inline py-12 text-6xl align-middle">
			finderFly
		</h1>
	</div>
	<a href="/mode" use:link class="items-center block pt-6">
		<button class="px-6 py-4 font-sans text-2xl rounded-lg">
			START
		</button>
	</a>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	h1 { 
		color: #F28E44;
	}
</style>