<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item> -->
    </a-breadcrumb>
    <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
      <a-row type="flex" justify="center" align="top" :gutter="16">
        <a-col v-for="req in requests" :key="req.id" :xs="8" :sm="8" :md="8" :lg="8">
          <a-card hoverable style="width: 240px;">
            <video controls style="max-width: 100%;">
              <source :src="req.video_url" type="video/mp4">
            </video>
            <template slot="actions" class="ant-card-actions">
              <a :href="`https://twitter.com/_/status/${req.status}`">
                <a-icon key="twitter" type="twitter" />
              </a>
              <a :href="req.video_url">
                <a-icon type="video-camera" />
              </a>
              <a-icon key="ellipsis" type="ellipsis" />
            </template>
          </a-card>
        </a-col>
      </a-row>
    </div>
  </div>
</template>
<script>
export default {
  async asyncData ({ app, params }) {
    console.log(app);
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
</style>
