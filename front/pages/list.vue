<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item> -->
    </a-breadcrumb>
    <div class="container">
      <figure v-for="req in requests" :key="req.id">
        <video controls>
          <source :src="req.video_url" type="video/mp4">
        </video>
        <figcaption><a :href="req.video_url"><a-icon type="zoom-in" /></a></figcaption>
      </figure>
    </div>
  </div>
</template>
<script>
export default {
  async asyncData ({ app, params }) {
    const data = await app.$service.listService.get();

    return {list: data}
  },
  computed: {
    requests() {
      return this.list
    }
  },
  methods: {}
};
</script>
<style>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
  vertical-align: top;
  color: white;
}
.spin-content {
  border: 1px solid #91d5ff;
  background-color: #e6f7ff;
  padding: 30px;
}
.container {
  display: flex;
  flex-wrap: wrap;
  background: #fff;
  padding: 0;
  min-height: 280px;
}
.container > figure {
  position: relative;
  flex-grow:1;
  display: flex;
  flex-direction: column;
  margin: 2px;
}
.container > figure > video {
  height: 250px;
  object-fit: cover;
  max-width: 100%;
  min-width: 100%;
}
.container > figure > figcaption {
  position: absolute;
  right: 5px;
  top: 1px;
  z-index: 1;
  font-size: 24px;
}
</style>
