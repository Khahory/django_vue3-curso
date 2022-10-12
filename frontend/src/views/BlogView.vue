<template>
  <div class="blog">
    <h1>This is BLOG</h1>
  </div>

  <div>
    {{APIData}}
  </div>
</template>

<script>
import { getAPi } from "@/axios-api";

export default {
  name: 'Blog',
  data() {
    return {
      APIData: []
    }
  },
  created() {
    getAPi.get('blog/posts')
        .then(res => {
          console.log('tenemos info yeaaaa')
          this.APIData = res.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>
