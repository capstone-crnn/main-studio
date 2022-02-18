<script>
	// Imports
	import { scaleLinear, scaleOrdinal } from "d3-scale";
  	import { extent } from "d3-array";
	import * as data from "../../data/subject4.js";	// TODO: temp data, remove later

	const height = 200;
	const width = 300;
	const buffer = 10;
	const colors = ["red", "green", "blue"];
	const axisSpace = 1;

	let xExtent = extent(data, (d) => d["X_Value"]);
    let yExtent = extent(data, (d) => d["radar24-I"]);
	
	let signals = new Set(json.map((d) => d["radar24-I"]));

    let xScale = scaleLinear()
      .domain(xExtent)
      .range([buffer + axisSpace, width - buffer]);
    let yScale = scaleLinear()
      .domain(yExtent)
      .range([height - buffer - axisSpace, buffer]);


    const dataObj = {
      data,
      xScale,
      yScale,
      signals: Array.from(signals),
    };

</script>

<main>
	<div id="graph" />

	<svg {height} {width}>
		{#each dataObj.data as item}
		  <circle
			r="3"
			cx={dataObj.xScale(item.petalLength)}
			cy={dataObj.yScale(item.petalWidth)} />
		{/each}
	
		{#each dataObj.xScale.ticks(5) as tick}
		  <g transform={`translate(${dataObj.xScale(tick)} ${height - 20})`}>
			<line y1="-5" y2="0" stroke="black" />
			<text y="20" text-anchor="middle">{tick}</text>
		  </g>
		{/each}
	
		{#each dataObj.yScale.ticks(5) as tick}
		  <g transform={`translate(0 ${dataObj.yScale(tick)})`}>
			<line x1="35" x2="40" stroke="black" />
			<text x="30" dominant-baseline="middle" text-anchor="end">{tick}</text>
		  </g>
		{/each}
	
		<g transform={`translate(${width - 100}, ${height - 100})`}>
		  {#each dataObj.species as species, i}
			<g transform={`translate(0 ${i * 20})`}>
			  <rect height="10" width="10" />
			  <text dominant-baseline="middle" y="5" x="20">{species}</text>
			</g>
		  {/each}
		</g>
	  </svg>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	
</style>