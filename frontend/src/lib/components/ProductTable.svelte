<script lang="ts">
  import ProductRow from "./ProductRow.svelte";
  let data = [
    {
      id: 1,
      productName: "Audio-Technica ATH-WP900 On-Ear Headphones (Flamed Maple)",
      price: "$699.00",
    },
    {
      id: 2,
      productName: "RTX 5090",
      price: "$599.99",
    },
  ];
</script>

<table>
  <tbody>
    <ProductRow isHeader={true} />
    {#each data as item (item.id)}
      <ProductRow isHeader={false} data={item} />
    {/each}
  </tbody>
</table>

<style>
  table {
    border: 1px solid;
    border-collapse: collapse;
    padding: 10px;
    text-align: center;
    font-size: 1em;
    min-width: 800px;
  }
</style>
