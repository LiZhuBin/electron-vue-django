<template>
    <el-card >
        <el-header>选择地区</el-header>
        <el-main>
        <el-transfer
                filterable
                :filter-method="filterMethod"
                filter-placeholder="请输入城市拼音"
                :titles="['省份', '选择查询']"
                @change="handleChange"
                v-model="value"
                :data="data">
        </el-transfer>
<div>{{check}}</div>
        </el-main>
    </el-card>

</template>

<script>

  export default {
    name: "LocationPage",
    cities : [],
    data() {
      this.cities = this.$store.state.cities;
      const generateData = _ => {
        const data = [];
        this.cities.forEach((city, index) => {
          data.push({
            label: city,
            key: index,
            cities: this.cities[index],
          });
        });
        return data;
      };
      return {

        data: generateData(),
        value: [],
        check: [],
        filterMethod(query, item) {
          return item.cities.indexOf(query) > -1;
        }
      };

    },
methods:{
  handleChange(value, direction, movedKeys) {
    this.check = value;
    this.$store.state.cities_select = value
  },


}
  }
</script>

<style scoped>

</style>