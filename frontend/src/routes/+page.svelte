<script lang="ts">
  import ProductTable from "$lib/components/ProductTable.svelte";
  import AddItemModal from "$lib/components/AddItemModal.svelte";

  let showModal = $state(false);
</script>

<div class="container">
  <AddItemModal bind:showModal />
  <h1>This is a place holder</h1>
  <p>Welcome to the page</p>
  <ProductTable addItemEvent={() => (showModal = true)} />
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
