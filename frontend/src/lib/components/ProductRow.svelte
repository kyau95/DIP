<script lang="ts">
  import Icon from "./Icon.svelte";
  let props = $props();
  let data = $derived(props.data);
</script>

{#if props.isHeader}
  <tr>
    <th>Product Name</th>
    <th>Tracker Price</th>
  </tr>
{:else}
  <tr>
    <td>{data["productName"]} <Icon /></td>
    <td>{data["price"]}</td>
  </tr>
{/if}

<style>
  th,
  td {
    border: 1px solid;
    text-align: center;
    padding: 12px 0;
  }
  tr {
    padding: 5px;
  }
</style>
