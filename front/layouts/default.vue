<template>
  <a-layout id="components-layout-demo-top" class="layout">
		<Header />
    <a-layout-content style="padding: 0 50px">
      <nuxt />
    </a-layout-content>
		<Footer />
  </a-layout>
</template>
<script>
	import Header from "@/components/header.vue"; // headerをインポート
	import Footer from "@/components/footer.vue"; // footerをインポート
	export default {
		components: {
			Header,
			Footer
		}
	};
</script>
<style lang="scss" scoped></style>
