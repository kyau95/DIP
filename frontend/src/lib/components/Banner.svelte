<script lang="ts">
  let { errorMessage, successMessage, isLoading } = $props();
</script>

{#if errorMessage || successMessage || isLoading}
  <div class="banner-container">
    {#if isLoading}
      <div class="banner loading">
        <span class="spinner"></span>
        Checking product details...
      </div>
    {/if}
    {#if errorMessage}
      <div class="banner error">
        <svg class="banner-icon" viewBox="0 0 20 20" fill="currentColor">
          <path
            fill-rule="evenodd"
            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
            clip-rule="evenodd"
          />
        </svg>
        {errorMessage}
      </div>
    {/if}
    {#if successMessage}
      <div class="banner success">
        <svg class="banner-icon" viewBox="0 0 20 20" fill="currentColor">
          <path
            fill-rule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
            clip-rule="evenodd"
          />
        </svg>
        {successMessage}
      </div>
    {/if}
  </div>
{/if}

<style>
  .banner-container {
    padding: 16px 24px 0 24px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .banner {
    display: flex;
    align-items: center;
    padding: 12px 16px;
    border-radius: var(--default-border-radius);
    font-size: 0.9rem;
    font-weight: 500;
    line-height: 1.4;
    border-width: 1px;
    border-style: solid;
  }

  .banner-icon {
    width: 20px;
    height: 20px;
    margin-right: 8px;
    flex-shrink: 0;
  }

  .loading {
    background-color: #f8fafc;
    border-color: #e2e8f0;
    color: #475569;
  }

  .error {
    background-color: #fff1f2;
    border-color: #fecdd3;
    color: #991b1b;
  }

  .success {
    background-color: #ecfdf5;
    border-color: #a7f3d0;
    color: #065f46;
  }

  .spinner {
    border: 2px solid #64748b;
    border-top: 2px solid transparent;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 0.8s linear infinite;
    margin-right: 8px;
    display: inline-block;
    vertical-align: middle;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
