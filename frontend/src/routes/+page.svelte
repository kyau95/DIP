<script lang="ts">
  import ProductTable from "$lib/components/ProductTable.svelte";
</script>

<div class="container">
  <h1>Sales Tracker</h1>
  <p>This page is to track the items and scrape new items</p>
  <ProductTable />
</div>

<style>
  .container {
    min-width: 800px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }
</style>
