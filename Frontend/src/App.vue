<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="container" style="margin-top: 30px;">
    <RouterView />
  </div>
</template>

<style>
@import "tailwindcss";
@import "tailwindcss-primeui";
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
* {
  font-family: "Roboto", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
  font-variation-settings:
      "wdth" 100;
}

.container {
  max-width: 1250px;
  margin: 0 auto;
}

body {
  background-color: rgba(0, 0, 0, 0.05);
}

:root {
  --p-primary-color: #8b8cff !important;
  --p-primary-hover-color: #9091ea !important;
  --p-primary-active-color: #9091ea !important;
  --p-form-field-float-label-focus-color: #8b8cff !important;
}
</style>