<template>
  <view class="content">
    <view class="header flexrow fab sac whitefont smallshadow" :style="headerStyle">
      <view class="center" style="width: 100rpx" @click="handleBack">
        <uni-icons :type="backIcon" color="white" size="26"></uni-icons>
      </view>
      <view class="custom-title --f1 rowcenter">{{ title }}</view>
      <view class="center" style="width: 100rpx" @click="handleMagic">
        <uni-icons type="smallcircle" color="white" size="26"></uni-icons>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '导航栏'
    },
    color: {
      type: String,
      default: 'blue'
    },
    isHome: {
      type: Boolean,
      default: false
    },
    height: {
      type: Number,
      default: 100
    }
    
  },
  data() {
    return {
      backIcon: 'undo-filled',
      headerStyle: {
        height: '100rpx',
        width: '100%',
        borderBottomLeftRadius: '20rpx',
        borderBottomRightRadius: '20rpx',
        borderTopLeftRadius: '0',
        borderTopRightRadius: '0',
        top: '0',
        left: '0',
        background: 'rgba(0, 95, 255, 0.8)'
      }
    };
  },
  methods: {
    // 导航栏事件
    handleBack() {
      if (this.isHome) {
        uni.navigateTo({
          url: '/#'
        })
      } else {
        uni.navigateBack();
      }
    },
    // 导航栏动画
    handleMagic() {
      this.headerStyle.height = this.headerStyle.height === '100rpx' ? '90rpx' : '100rpx';
      this.headerStyle.width = this.headerStyle.width === '100%' ? '95%' : '100%';
      this.headerStyle.borderTopLeftRadius = this.headerStyle.borderTopLeftRadius === '0' ? '30rpx' : '0';
      this.headerStyle.borderTopRightRadius = this.headerStyle.borderTopRightRadius === '0' ? '30rpx' : '0';
      this.headerStyle.borderBottomLeftRadius = this.headerStyle.borderBottomLeftRadius === '20rpx' ? '30rpx' : '20rpx';
      this.headerStyle.borderBottomRightRadius = this.headerStyle.borderBottomRightRadius === '20rpx' ? '30rpx' : '20rpx';
      this.headerStyle.top = this.headerStyle.top === '0' ? '10rpx' : '0';
      this.headerStyle.left = this.headerStyle.left === '0' ? 'calc(0.025 * 100vw)' : '0';
    }
  },
  mounted() {
    if (this.color === 'blue') {
      this.headerStyle.background = 'rgba(0, 95, 255, 0.8)';
    } else if (this.color === 'green') {
      this.headerStyle.background = 'rgba(43, 153, 57, 0.8)';
    }
    this.headerStyle.height = this.height + 'rpx'
    if (this.isHome === true) {
      this.backIcon = 'home-filled'
    }
  }
};
</script>

<style scoped>
@import '../../static/css/global.scss';
/* 导航栏样式 */
.header {
  box-sizing: border-box;
  position: fixed;
  padding: 0 5rpx;
  backdrop-filter: blur(10rpx);
  transition: 0.5s all;
}
</style>
