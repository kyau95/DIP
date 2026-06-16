<script lang="ts">
	const { url = "https://example.com" } = $props();
</script>

<a href={url} target="_blank">
	<svg
		xmlns="http://w3.org"
		viewBox="0 0 32 32"
		width="20px"
		height="20px"
		fill="none"
		stroke="currentColor"
		stroke-width="3"
		stroke-linecap="round"
		stroke-linejoin="round"
	>
		<!-- The Box -->
		<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
		<!-- The Arrow -->
		<polyline points="15 3 21 3 21 9" />
		<line x1="10" y1="14" x2="21" y2="3" />
	</svg>
</a>

<style>
	svg {
		padding-top: 1px;
		padding-left: 5px;
		cursor: pointer;
		display: inline-block;
		vertical-align: middle;
		color: #525151;
	}

	svg:hover {
		color: #111827;
	}

	svg:active {
		transform: scale(0.95);
	}
</style>
