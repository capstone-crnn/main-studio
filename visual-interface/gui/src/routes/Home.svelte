<script>
	// Imports
	import { Link } from "svelte-routing";

	// Props
	export let name;

	let version;
	const get_version = async () => {
		version = await api.GetVersion();
	}
</script>

<main>
	<h1>{name} Logo</h1>
	<Link to="mode">
		<button>START</button>
	</Link>
</main>

<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;


</style>