<script lang="ts">
  import Icon from "./Icon.svelte";
  
  const props = $props();
  const data = $derived(props.data);
  const currencySymbol: string = $derived(props.currency || "$");
  const price: string = $derived(
    data ? `${currencySymbol}${parseFloat(data["price"]).toFixed(2)}` : ""
  );
</script>

<!-- TODO: Take in an image URL, user can hover over the product name column and see the item-->

{#if props.isHeader}
  <tr>
    <th>Product Name</th>
    <th>Tracker Price</th>
  </tr>
{:else}
  <tr>
    <td>
      {data["productName"]}
      <Icon url={data["productUrl"]} />
    </td>
    <td>{price}</td>
  </tr>
{/if}

<style>
  tr {
    transition: background-color 0.15s ease;
  }

  tr:hover {
    background-color: #f8fafc;
  }

  th {
    background-color: #f8fafc;
    color: #475569;
    font-weight: 600;
    padding: 16px 24px;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
  }

  td {
    padding: 16px 24px;
    border-bottom: 1px solid #f1f5f9;
    color: #1e293b;
    text-overflow: ellipsis;
    overflow: hidden;
  }

  /* Removes the bottom border from the very last row */
  tr:last-child td {
    border-bottom: none;
  }
</style>
