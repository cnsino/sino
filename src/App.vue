<!-- The exported code uses Tailwind CSS. Install Tailwind CSS in your dev environment to ensure all styles work. -->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- 顶部导航栏 -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <div
        class="container mx-auto px-4 flex items-center justify-between h-16"
      >
        <div class="flex items-center space-x-4">
          <div class="text-2xl font-bold text-blue-600 flex items-center">
            <el-icon class="mr-2"><Monitor /></el-icon>
            <span>聚合工坊</span>
          </div>
          <nav class="hidden md:flex space-x-8 ml-8">
            <a
              href="#"
              class="text-gray-700 hover:text-blue-600 font-medium cursor-pointer"
              >首页</a
            >
            <a
              href="#tools"
              class="text-gray-700 hover:text-blue-600 font-medium cursor-pointer"
              >工具</a
            >
            <a
              href="#games"
              class="text-gray-700 hover:text-blue-600 font-medium cursor-pointer"
              >游戏</a
            >
            <a
              href="#"
              class="text-gray-700 hover:text-blue-600 font-medium cursor-pointer"
              >社区</a
            >
            <a
              href="#"
              class="text-gray-700 hover:text-blue-600 font-medium cursor-pointer"
              >排行榜</a
            >
          </nav>
        </div>
        <div class="flex items-center space-x-4">
          <div class="relative">
            <input
              type="text"
              placeholder="搜索工具和游戏..."
              class="pl-10 pr-4 py-2 border-none rounded-full bg-gray-100 focus:bg-white focus:ring-2 focus:ring-blue-500 w-64 text-sm"
            />
            <el-icon class="absolute left-3 top-2.5 text-gray-400"
              ><Search
            /></el-icon>
          </div>
          <button
            class="bg-blue-600 text-white px-4 py-2 rounded-full text-sm font-medium hover:bg-blue-700 transition !rounded-button whitespace-nowrap cursor-pointer"
          >
            <el-icon class="mr-1"><Plus /></el-icon>
            上传工具
          </button>
          <div class="flex items-center space-x-2 cursor-pointer">
            <img
              :src="userAvatar"
              alt="用户头像"
              class="w-8 h-8 rounded-full object-cover"
            />
            <span class="text-sm font-medium text-gray-700 hidden md:inline">{{
              username
            }}</span>
          </div>
        </div>
      </div>
    </header>
    <!-- Hero 区域 -->
    <div class="relative overflow-hidden" style="height: 500px">
      <img
        src="/img_14.jpg"
        alt="聚合工坊背景"
        class="absolute inset-0 w-full h-full object-cover object-top"
      />
      <div
        class="absolute inset-0 bg-gradient-to-r from-blue-900/80 to-transparent"
      >
        <div class="container mx-auto px-4 h-full flex items-center">
          <div class="max-w-xl text-white">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">
              一站式工具与游戏聚合平台
            </h1>
            <p class="text-xl mb-8 text-blue-100">
              发现、使用和分享各种实用工具与有趣游戏，满足您的所有需求
            </p>
            <div class="flex space-x-4">
              <button
                class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full font-medium text-lg transition !rounded-button whitespace-nowrap cursor-pointer"
              >
                立即探索
              </button>
              <button
                class="bg-white/20 hover:bg-white/30 backdrop-blur-sm text-white px-6 py-3 rounded-full font-medium text-lg transition !rounded-button whitespace-nowrap cursor-pointer"
              >
                了解更多
              </button>
            </div>
            <div class="mt-8 flex items-center space-x-4">
              <div class="flex -space-x-2">
                <img
                  v-for="(avatar, index) in userAvatars"
                  :key="index"
                  :src="avatar"
                  alt="用户头像"
                  class="w-8 h-8 rounded-full border-2 border-blue-900 object-cover"
                />
              </div>
              <p class="text-blue-100">
                已有 <span class="font-bold">12,580+</span> 用户加入我们
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 主要内容区域 -->
    <div class="container mx-auto px-4 py-12">
      <!-- 数据统计卡片 -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        <div
          v-for="(stat, index) in statistics"
          :key="index"
          class="bg-white rounded-xl shadow-sm p-6 flex items-center space-x-4 hover:shadow-md transition"
        >
          <div :class="`rounded-full p-3 ${stat.bgColor}`">
            <el-icon :size="24" :class="stat.iconColor"
              ><component :is="stat.icon"
            /></el-icon>
          </div>
          <div>
            <div class="text-2xl font-bold">{{ stat.value }}</div>
            <div class="text-gray-500 text-sm">{{ stat.label }}</div>
          </div>
        </div>
      </div>
      <!-- 工具和游戏内容区域 -->
      <div class="flex flex-col md:flex-row gap-8 mb-16">
        <!-- 左侧导航 -->
        <div class="md:w-64 flex-shrink-0 sticky top-20 self-start">
          <!-- 工具分类导航 -->
          <div class="bg-white rounded-xl shadow-sm p-4 mb-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center">
              <el-icon class="mr-2"><Tools /></el-icon>
              工具分类
            </h3>
            <ul class="space-y-2">
              <li v-for="(category, index) in toolCategories" :key="index">
                <button
                  :class="`w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition cursor-pointer flex items-center ${
                    activeToolCategory === category.id
                      ? 'bg-blue-100 text-blue-700'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`"
                  @click="activeToolCategory = category.id"
                >
                  <el-icon
                    class="mr-2"
                    v-if="activeToolCategory === category.id"
                    ><Check
                  /></el-icon>
                  <span>{{ category.name }}</span>
                </button>
              </li>
            </ul>
          </div>
          <!-- 游戏分类导航 -->
          <div class="bg-white rounded-xl shadow-sm p-4 mb-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center">
              <el-icon class="mr-2"><GameController /></el-icon>
              游戏分类
            </h3>
            <ul class="space-y-2">
              <li v-for="(category, index) in gameCategories" :key="index">
                <button
                  :class="`w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition cursor-pointer flex items-center ${
                    activeGameCategory === category.id
                      ? 'bg-green-100 text-green-700'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`"
                  @click="activeGameCategory = category.id"
                >
                  <el-icon
                    class="mr-2"
                    v-if="activeGameCategory === category.id"
                    ><Check
                  /></el-icon>
                  <span>{{ category.name }}</span>
                </button>
              </li>
            </ul>
          </div>
          <!-- 热门标签 -->
          <div class="bg-white rounded-xl shadow-sm p-4">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center">
              <el-icon class="mr-2"><Collection /></el-icon>
              热门标签
            </h3>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="(tag, index) in popularTags"
                :key="index"
                class="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-xs font-medium hover:bg-gray-200 transition cursor-pointer"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
        <!-- 右侧内容区域 -->
        <div class="flex-1">
          <!-- 工具聚合模块 -->
          <section id="tools" class="mb-12">
            <div class="mb-8">
              <div class="flex justify-between items-center mb-4">
                <h2 class="text-2xl font-bold text-gray-800 flex items-center">
                  <el-icon class="mr-2"><Tools /></el-icon>
                  {{ currentCategoryName }}
                </h2>
                <a
                  href="/img_34.jpg"
                  data-readdy="true"
                  class="px-4 py-2 rounded-full text-sm font-medium bg-gray-100 text-gray-700 hover:bg-gray-200 transition !rounded-button whitespace-nowrap cursor-pointer inline-flex items-center"
                >
                  查看全部
                  <el-icon class="ml-1"><ArrowRight /></el-icon>
                </a>
              </div>
              <p class="text-gray-500 text-sm mb-6">
                当前显示 {{ filteredTools.length }} 个{{
                  currentCategoryName
                }}，点击工具卡片查看详情
              </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div
                v-for="(tool, index) in filteredTools"
                :key="index"
                class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition group cursor-pointer"
              >
                <div class="h-40 overflow-hidden relative">
                  <img
                    :src="tool.image"
                    :alt="tool.name"
                    class="w-full h-full object-cover object-top transition-transform duration-500 group-hover:scale-105"
                  />
                  <div class="absolute top-3 right-3">
                    <button
                      class="bg-white/80 backdrop-blur-sm p-2 rounded-full hover:bg-white transition !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      <el-icon
                        :class="
                          tool.isFavorite ? 'text-red-500' : 'text-gray-600'
                        "
                        ><Star
                      /></el-icon>
                    </button>
                  </div>
                  <div
                    class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4"
                  >
                    <div class="flex items-center space-x-2">
                      <span
                        class="text-xs font-medium px-2 py-1 rounded-full bg-blue-600/90 text-white"
                        >{{ getCategoryName(tool.categoryId) }}</span
                      >
                      <span
                        class="text-xs font-medium px-2 py-1 rounded-full bg-white/20 text-white flex items-center"
                      >
                        <el-icon class="mr-1"><View /></el-icon>
                        {{ tool.views }}
                      </span>
                    </div>
                  </div>
                </div>
                <div class="p-4">
                  <h3 class="text-lg font-semibold mb-1 text-gray-800">
                    {{ tool.name }}
                  </h3>
                  <p class="text-gray-500 text-sm mb-3 line-clamp-2">
                    {{ tool.description }}
                  </p>
                  <div class="flex items-center justify-between">
                    <div class="flex items-center">
                      <el-icon class="text-yellow-500 mr-1"><Star /></el-icon>
                      <span class="text-sm font-medium">{{ tool.rating }}</span>
                    </div>
                    <button
                      class="text-blue-600 hover:text-blue-800 text-sm font-medium flex items-center !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      立即使用
                      <el-icon class="ml-1"><ArrowRight /></el-icon>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <!-- 游戏聚合模块 -->
          <section id="games" class="mb-12">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-bold text-gray-800 flex items-center">
                <el-icon class="mr-2"><GameController /></el-icon>
                热门游戏
              </h2>
              <a
                href="/img_34.jpg"
                data-readdy="true"
                class="px-4 py-2 rounded-full text-sm font-medium bg-gray-100 text-gray-700 hover:bg-gray-200 transition !rounded-button whitespace-nowrap cursor-pointer inline-flex items-center"
              >
                查看全部
                <el-icon class="ml-1"><ArrowRight /></el-icon>
              </a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div
                v-for="(game, index) in filteredGames"
                :key="index"
                class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition group cursor-pointer"
              >
                <div class="h-52 overflow-hidden relative">
                  <img
                    :src="game.image"
                    :alt="game.name"
                    class="w-full h-full object-cover object-top transition-transform duration-500 group-hover:scale-105"
                  />
                  <div class="absolute top-3 right-3">
                    <button
                      class="bg-white/80 backdrop-blur-sm p-2 rounded-full hover:bg-white transition !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      <el-icon
                        :class="
                          game.isFavorite ? 'text-red-500' : 'text-gray-600'
                        "
                        ><Star
                      /></el-icon>
                    </button>
                  </div>
                  <div
                    class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4"
                  >
                    <div class="flex items-center space-x-2">
                      <span
                        class="text-xs font-medium px-2 py-1 rounded-full bg-green-600/90 text-white"
                        >{{ getGameCategoryName(game.categoryId) }}</span
                      >
                      <span
                        class="text-xs font-medium px-2 py-1 rounded-full bg-white/20 text-white flex items-center"
                      >
                        <el-icon class="mr-1"><User /></el-icon>
                        {{ game.players }} 在线
                      </span>
                    </div>
                  </div>
                </div>
                <div class="p-4">
                  <h3 class="text-lg font-semibold mb-1 text-gray-800">
                    {{ game.name }}
                  </h3>
                  <p class="text-gray-500 text-sm mb-3 line-clamp-2">
                    {{ game.description }}
                  </p>
                  <div class="flex items-center justify-between">
                    <div class="flex items-center">
                      <el-icon class="text-yellow-500 mr-1"><Star /></el-icon>
                      <span class="text-sm font-medium">{{ game.rating }}</span>
                    </div>
                    <button
                      class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-full text-sm font-medium transition !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      开始游戏
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
      <!-- 分类导航 -->
      <section class="mb-16">
        <div class="flex flex-col md:flex-row gap-8">
          <div class="md:w-64 flex-shrink-0">
            <div class="bg-white rounded-xl shadow-sm p-4 sticky top-20">
              <h2
                class="text-xl font-bold text-gray-800 mb-6 flex items-center"
              >
                <el-icon class="mr-2"><Collection /></el-icon>
                分类导航
              </h2>
              <ul class="space-y-3">
                <li
                  v-for="(category, index) in allCategories"
                  :key="index"
                  class="flex items-center justify-between p-2 rounded-lg hover:bg-gray-50 transition cursor-pointer"
                >
                  <span class="font-medium text-gray-700">{{
                    category.name
                  }}</span>
                  <span class="text-sm text-gray-500">{{
                    category.count
                  }}</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="flex-1">
            <h2 class="text-2xl font-bold text-gray-800 mb-8 flex items-center">
              <el-icon class="mr-2"><Collection /></el-icon>
              分类导航
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div
                v-for="(category, index) in allCategories"
                :key="index"
                class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition cursor-pointer group"
              >
                <div class="h-32 overflow-hidden relative">
                  <img
                    :src="category.image"
                    :alt="category.name"
                    class="w-full h-full object-cover object-top transition-transform duration-500 group-hover:scale-105"
                  />
                  <div
                    class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-4"
                  >
                    <h3 class="text-white font-medium">{{ category.name }}</h3>
                  </div>
                </div>
                <div class="p-3">
                  <div class="flex items-center justify-between">
                    <span class="text-sm text-gray-500"
                      >{{ category.count }} 个项目</span
                    >
                    <el-icon
                      class="text-gray-400 group-hover:text-blue-600 transition-colors"
                      ><ArrowRight
                    /></el-icon>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- 用户成就与排行榜 -->
      <section class="mb-16">
        <div class="flex flex-col md:flex-row gap-8">
          <div class="md:w-64 flex-shrink-0">
            <div class="bg-white rounded-xl shadow-sm p-4 sticky top-20">
              <h2
                class="text-xl font-bold text-gray-800 mb-6 flex items-center"
              >
                <el-icon class="mr-2"><List /></el-icon>
                积分排行榜
              </h2>
              <div class="space-y-4">
                <div
                  v-for="(user, index) in leaderboard"
                  :key="index"
                  class="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-50 transition cursor-pointer"
                >
                  <div
                    :class="`w-6 h-6 rounded-full flex items-center justify-center font-medium ${
                      index < 3
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-100 text-gray-700'
                    }`"
                  >
                    {{ index + 1 }}
                  </div>
                  <img
                    :src="user.avatar"
                    :alt="user.name"
                    class="w-8 h-8 rounded-full object-cover"
                  />
                  <div class="flex-1">
                    <div class="font-medium text-gray-800 text-sm">
                      {{ user.name }}
                    </div>
                  </div>
                  <div class="text-sm font-medium text-blue-600">
                    {{ user.points }}
                  </div>
                </div>
              </div>
              <div class="mt-4 text-center">
                <button
                  class="text-blue-600 hover:text-blue-800 text-sm font-medium !rounded-button whitespace-nowrap cursor-pointer"
                >
                  查看完整排行榜
                  <el-icon class="ml-1"><ArrowRight /></el-icon>
                </button>
              </div>
            </div>
          </div>
          <div class="flex-1">
            <div class="bg-white rounded-xl shadow-sm p-6">
              <h2
                class="text-xl font-bold text-gray-800 mb-6 flex items-center"
              >
                <el-icon class="mr-2"><Trophy /></el-icon>
                最新成就
              </h2>
              <div class="space-y-4">
                <div
                  v-for="(achievement, index) in achievements"
                  :key="index"
                  class="flex items-center space-x-4 p-3 rounded-lg hover:bg-gray-50 transition cursor-pointer"
                >
                  <div :class="`rounded-full p-3 ${achievement.bgColor}`">
                    <el-icon :size="20" :class="achievement.iconColor"
                      ><component :is="achievement.icon"
                    /></el-icon>
                  </div>
                  <div class="flex-1">
                    <h3 class="font-medium text-gray-800">
                      {{ achievement.title }}
                    </h3>
                    <p class="text-sm text-gray-500">
                      {{ achievement.description }}
                    </p>
                  </div>
                  <div class="text-right">
                    <div class="text-xs text-gray-500">
                      {{ achievement.date }}
                    </div>
                    <div class="text-sm font-medium text-blue-600">
                      +{{ achievement.points }} 积分
                    </div>
                  </div>
                </div>
              </div>
              <div class="mt-4 text-center">
                <button
                  class="text-blue-600 hover:text-blue-800 text-sm font-medium !rounded-button whitespace-nowrap cursor-pointer"
                >
                  查看全部成就
                  <el-icon class="ml-1"><ArrowRight /></el-icon>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- 最新动态与社区 -->
      <section class="mb-16">
        <div class="flex flex-col md:flex-row gap-8">
          <div class="md:w-64 flex-shrink-0">
            <div class="bg-white rounded-xl shadow-sm p-4 sticky top-20">
              <h2
                class="text-xl font-bold text-gray-800 mb-6 flex items-center"
              >
                <el-icon class="mr-2"><ChatDotRound /></el-icon>
                社区分类
              </h2>
              <ul class="space-y-3">
                <li
                  v-for="(category, index) in [
                    '全部',
                    '教程',
                    '推荐',
                    '经验分享',
                    '问答',
                    '资源',
                  ]"
                  :key="index"
                  class="flex items-center p-2 rounded-lg hover:bg-gray-50 transition cursor-pointer"
                >
                  <span class="font-medium text-gray-700">{{ category }}</span>
                </li>
              </ul>
              <div class="mt-6">
                <button
                  class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full font-medium text-sm w-full transition !rounded-button whitespace-nowrap cursor-pointer"
                >
                  发布内容
                </button>
              </div>
            </div>
          </div>
          <div class="flex-1">
            <h2 class="text-2xl font-bold text-gray-800 mb-8 flex items-center">
              <el-icon class="mr-2"><ChatDotRound /></el-icon>
              社区动态
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                v-for="(post, index) in communityPosts"
                :key="index"
                class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition cursor-pointer"
              >
                <div class="h-48 overflow-hidden">
                  <img
                    :src="post.image"
                    :alt="post.title"
                    class="w-full h-full object-cover object-top"
                  />
                </div>
                <div class="p-4">
                  <div class="flex items-center space-x-2 mb-3">
                    <span
                      class="text-xs font-medium px-2 py-1 rounded-full bg-blue-100 text-blue-700"
                      >{{ post.category }}</span
                    >
                    <span class="text-xs text-gray-500">{{ post.date }}</span>
                  </div>
                  <h3 class="text-lg font-semibold mb-2 text-gray-800">
                    {{ post.title }}
                  </h3>
                  <p class="text-gray-500 text-sm mb-4 line-clamp-2">
                    {{ post.content }}
                  </p>
                  <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                      <img
                        :src="post.author.avatar"
                        :alt="post.author.name"
                        class="w-6 h-6 rounded-full object-cover"
                      />
                      <span class="text-sm text-gray-700">{{
                        post.author.name
                      }}</span>
                    </div>
                    <div class="flex items-center space-x-3 text-gray-500">
                      <div class="flex items-center">
                        <el-icon class="mr-1"><ChatLineRound /></el-icon>
                        <span class="text-xs">{{ post.comments }}</span>
                      </div>
                      <div class="flex items-center">
                        <el-icon class="mr-1"><View /></el-icon>
                        <span class="text-xs">{{ post.views }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-8 text-center">
              <button
                class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full font-medium transition !rounded-button whitespace-nowrap cursor-pointer"
              >
                进入社区
                <el-icon class="ml-1"><ArrowRight /></el-icon>
              </button>
            </div>
          </div>
        </div>
      </section>
      <!-- 加入我们 -->
      <section class="mb-16">
        <div class="flex flex-col md:flex-row gap-8">
          <div class="md:w-64 flex-shrink-0">
            <div class="bg-white rounded-xl shadow-sm p-4 sticky top-20">
              <h2
                class="text-xl font-bold text-gray-800 mb-6 flex items-center"
              >
                <el-icon class="mr-2"><Connection /></el-icon>
                开发者资源
              </h2>
              <ul class="space-y-3">
                <li
                  v-for="(resource, index) in [
                    '开发文档',
                    'API 接口',
                    '开发工具',
                    '案例分享',
                    '常见问题',
                  ]"
                  :key="index"
                  class="flex items-center p-2 rounded-lg hover:bg-gray-50 transition cursor-pointer"
                >
                  <span class="font-medium text-gray-700">{{ resource }}</span>
                </li>
              </ul>
              <div class="mt-6">
                <button
                  class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full font-medium text-sm w-full transition !rounded-button whitespace-nowrap cursor-pointer"
                >
                  申请开发者
                </button>
              </div>
            </div>
          </div>
          <div class="flex-1">
            <div
              class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-2xl overflow-hidden relative"
            >
              <div
                class="absolute right-0 top-0 bottom-0 w-1/3 overflow-hidden"
              >
                <img
                  src="/img_12.jpg"
                  alt="加入我们背景"
                  class="h-full w-full object-cover object-top"
                />
              </div>
              <div class="p-8 md:p-12 relative z-10">
                <div class="max-w-2xl">
                  <h2 class="text-3xl font-bold text-white mb-4">
                    加入我们的开发者社区
                  </h2>
                  <p class="text-blue-100 mb-8">
                    分享您的工具和游戏，与全球用户互动，获得反馈并提升您的创作。我们提供完善的开发支持和推广渠道。
                  </p>
                  <div class="flex flex-wrap gap-4">
                    <button
                      class="bg-white text-blue-700 hover:bg-blue-50 px-6 py-3 rounded-full font-medium transition !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      成为开发者
                    </button>
                    <button
                      class="bg-blue-700/30 hover:bg-blue-700/40 text-white px-6 py-3 rounded-full font-medium backdrop-blur-sm transition !rounded-button whitespace-nowrap cursor-pointer"
                    >
                      了解更多
                    </button>
                  </div>
                  <div class="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg">
                      <div class="text-white mb-2 flex items-center">
                        <el-icon class="mr-2"><Connection /></el-icon>
                        <span class="font-medium">全球用户</span>
                      </div>
                      <p class="text-blue-100 text-sm">
                        接触来自世界各地的用户，获得更广泛的曝光
                      </p>
                    </div>
                    <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg">
                      <div class="text-white mb-2 flex items-center">
                        <el-icon class="mr-2"><Money /></el-icon>
                        <span class="font-medium">收益分成</span>
                      </div>
                      <p class="text-blue-100 text-sm">
                        通过您的创作获得持续的收益分成和奖励
                      </p>
                    </div>
                    <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg">
                      <div class="text-white mb-2 flex items-center">
                        <el-icon class="mr-2"><DataAnalysis /></el-icon>
                        <span class="font-medium">数据分析</span>
                      </div>
                      <p class="text-blue-100 text-sm">
                        获取详细的用户数据和使用分析，优化您的作品
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <!-- 页脚 -->
    <footer class="bg-gray-900 text-white py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
          <div>
            <div class="text-2xl font-bold text-white mb-4 flex items-center">
              <el-icon class="mr-2"><Monitor /></el-icon>
              聚合工坊
            </div>
            <p class="text-gray-400 mb-4">
              一站式工具与游戏聚合平台，为您提供最优质的在线资源。
            </p>
            <div class="flex space-x-4">
              <a
                href="#"
                class="text-gray-400 hover:text-white transition cursor-pointer"
              >
                <el-icon :size="20"><Position /></el-icon>
              </a>
              <a
                href="#"
                class="text-gray-400 hover:text-white transition cursor-pointer"
              >
                <el-icon :size="20"><ChatDotRound /></el-icon>
              </a>
              <a
                href="#"
                class="text-gray-400 hover:text-white transition cursor-pointer"
              >
                <el-icon :size="20"><Share /></el-icon>
              </a>
              <a
                href="#"
                class="text-gray-400 hover:text-white transition cursor-pointer"
              >
                <el-icon :size="20"><Link /></el-icon>
              </a>
            </div>
          </div>
          <div>
            <h3 class="text-lg font-semibold mb-4">快速链接</h3>
            <ul class="space-y-2">
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >关于我们</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >联系我们</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >使用条款</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >隐私政策</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >常见问题</a
                >
              </li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-semibold mb-4">分类</h3>
            <ul class="space-y-2">
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >生活工具</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >学习工具</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >创意工具</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >开发工具</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="text-gray-400 hover:text-white transition cursor-pointer"
                  >休闲游戏</a
                >
              </li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-semibold mb-4">订阅更新</h3>
            <p class="text-gray-400 mb-4">
              订阅我们的新闻通讯，获取最新工具和游戏更新。
            </p>
            <div class="flex">
              <input
                type="email"
                placeholder="您的邮箱地址"
                class="bg-gray-800 text-white px-4 py-2 rounded-l-lg border-none focus:ring-2 focus:ring-blue-500 w-full text-sm"
              />
              <button
                class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-r-lg transition !rounded-button whitespace-nowrap cursor-pointer"
              >
                订阅
              </button>
            </div>
          </div>
        </div>
        <div
          class="pt-8 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center"
        >
          <div class="text-gray-400 text-sm mb-4 md:mb-0">
            &copy; 2025 聚合工坊. 保留所有权利.
          </div>
          <div class="flex items-center space-x-4">
            <span class="text-gray-400 text-sm">支持付款方式:</span>
            <div class="flex space-x-2">
              <el-icon :size="20" class="text-gray-400"><CreditCard /></el-icon>
              <el-icon :size="20" class="text-gray-400"><Wallet /></el-icon>
              <el-icon :size="20" class="text-gray-400"><Money /></el-icon>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>
<script lang="ts" setup>
import { ref, computed } from "vue";
import {
  Monitor,
  Search,
  Plus,
  Star,
  View,
  Tools,
  GameController,
  ArrowRight,
  Collection,
  Trophy,
  List,
  ChatDotRound,
  ChatLineRound,
  Connection,
  Money,
  DataAnalysis,
  Position,
  Share,
  Link,
  CreditCard,
  Wallet,
  User,
  Check,
} from "@element-plus/icons-vue";
// 用户信息
const username = ref("张小明");
const userAvatar = ref(
  "/img_9.jpg"
);
// 用户头像数组
const userAvatars = [
  "/img_21.jpg",
  "/img_36.jpg",
  "/img_25.jpg",
  "/img_18.jpg",
];
// 数据统计
const statistics = [
  {
    label: "工具总数",
    value: "1,280+",
    icon: "Tools",
    bgColor: "bg-blue-100",
    iconColor: "text-blue-600",
  },
  {
    label: "游戏总数",
    value: "850+",
    icon: "GameController",
    bgColor: "bg-green-100",
    iconColor: "text-green-600",
  },
  {
    label: "活跃用户",
    value: "12K+",
    icon: "User",
    bgColor: "bg-purple-100",
    iconColor: "text-purple-600",
  },
  {
    label: "开发者",
    value: "320+",
    icon: "Connection",
    bgColor: "bg-orange-100",
    iconColor: "text-orange-600",
  },
];
// 工具分类
const toolCategories = [
  { id: "all", name: "全部" },
  { id: "life", name: "生活工具" },
  { id: "study", name: "学习工具" },
  { id: "creative", name: "创意工具" },
  { id: "dev", name: "开发工具" },
];
const activeToolCategory = ref("all");
// 工具数据
const tools = [
  {
    id: 1,
    name: "汇率换算器",
    description:
      "实时汇率转换，支持全球 170+ 货币，历史汇率查询和汇率走势图表分析。",
    image:
      "/img_11.jpg",
    categoryId: "life",
    rating: 4.8,
    views: "25.6K",
    isFavorite: true,
  },
  {
    id: 2,
    name: "公式计算器",
    description:
      "支持数学、物理、化学等学科的公式计算，可保存常用公式和计算历史。",
    image:
      "/img_30.jpg",
    categoryId: "study",
    rating: 4.7,
    views: "18.3K",
    isFavorite: false,
  },
  {
    id: 3,
    name: "AI 图片生成器",
    description:
      "基于最新 AI 技术的图片生成工具，只需输入文字描述，即可创建高质量图像。",
    image:
      "/img_7.jpg",
    categoryId: "creative",
    rating: 4.9,
    views: "42.1K",
    isFavorite: true,
  },
  {
    id: 4,
    name: "JSON 格式化工具",
    description: "在线 JSON 格式化、验证、编辑工具，支持语法高亮和结构树展示。",
    image:
      "/img_1.jpg",
    categoryId: "dev",
    rating: 4.6,
    views: "15.8K",
    isFavorite: false,
  },
  {
    id: 5,
    name: "日历与日程规划",
    description: "集成日历、待办事项和提醒功能，帮助您高效管理时间和安排日程。",
    image:
      "/img_2.jpg",
    categoryId: "life",
    rating: 4.5,
    views: "20.3K",
    isFavorite: true,
  },
  {
    id: 6,
    name: "语言翻译工具",
    description: "支持 100+ 种语言互译，具备语音识别、实时翻译和离线翻译功能。",
    image:
      "/img_32.jpg",
    categoryId: "study",
    rating: 4.7,
    views: "32.5K",
    isFavorite: false,
  },
];
// 过滤工具
const filteredTools = computed(() => {
  if (activeToolCategory.value === "all") {
    return tools;
  }
  const filtered = tools.filter(
    (tool) => tool.categoryId === activeToolCategory.value
  );
  return filtered;
});

// 获取当前选中分类名称
const currentCategoryName = computed(() => {
  const category = toolCategories.find(
    (c) => c.id === activeToolCategory.value
  );
  return category ? category.name : "全部工具";
});
// 获取分类名称
const getCategoryName = (categoryId: string) => {
  const category = toolCategories.find((c) => c.id === categoryId);
  return category ? category.name : "";
};
// 游戏分类
const gameCategories = [
  { id: "all", name: "全部" },
  { id: "casual", name: "休闲游戏" },
  { id: "classic", name: "经典游戏" },
  { id: "multiplayer", name: "多人游戏" },
];
const activeGameCategory = ref("all");
// 游戏数据
const games = [
  {
    id: 1,
    name: "2048 数字方块",
    description: "经典数字益智游戏，通过滑动合并相同数字，挑战最高分数。",
    image:
      "/img_33.jpg",
    categoryId: "casual",
    rating: 4.7,
    players: "3.2K",
    isFavorite: true,
  },
  {
    id: 2,
    name: "贪吃蛇大作战",
    description: "重温经典贪吃蛇游戏，全新多人对战模式，争夺地盘成为最长的蛇。",
    image:
      "/img_24.jpg",
    categoryId: "classic",
    rating: 4.6,
    players: "5.8K",
    isFavorite: false,
  },
  {
    id: 3,
    name: "太空大战 IO",
    description:
      "多人在线太空射击游戏，驾驶飞船与全球玩家对战，升级武器取得胜利。",
    image:
      "/img_10.jpg",
    categoryId: "multiplayer",
    rating: 4.8,
    players: "7.5K",
    isFavorite: true,
  },
  {
    id: 4,
    name: "消除星星",
    description: "点击相同颜色的星星进行消除，挑战不同难度关卡，轻松有趣。",
    image:
      "/img_16.jpg",
    categoryId: "casual",
    rating: 4.5,
    players: "2.9K",
    isFavorite: false,
  },
  {
    id: 5,
    name: "俄罗斯方块",
    description:
      "经典俄罗斯方块游戏，支持多种游戏模式和难度，挑战您的反应能力。",
    image:
      "/img_8.jpg",
    categoryId: "classic",
    rating: 4.9,
    players: "4.3K",
    isFavorite: true,
  },
  {
    id: 6,
    name: "卡牌对决",
    description:
      "策略卡牌对战游戏，收集不同能力的卡牌，与其他玩家进行回合制对决。",
    image:
      "/img_3.jpg",
    categoryId: "multiplayer",
    rating: 4.7,
    players: "6.1K",
    isFavorite: false,
  },
];
// 过滤游戏
const filteredGames = computed(() => {
  if (activeGameCategory.value === "all") {
    return games;
  }
  return games.filter((game) => game.categoryId === activeGameCategory.value);
});
// 获取游戏分类名称
const getGameCategoryName = (categoryId: string) => {
  const category = gameCategories.find((c) => c.id === categoryId);
  return category ? category.name : "";
};
// 热门标签
const popularTags = [
  "效率工具",
  "图片处理",
  "文档编辑",
  "视频剪辑",
  "数据分析",
  "益智游戏",
  "动作游戏",
  "策略游戏",
  "学习工具",
  "社交工具",
  "音频处理",
  "开发工具",
];
// 所有分类
const allCategories = [
  {
    name: "生活工具",
    count: 248,
    image:
      "/img_22.jpg",
  },
  {
    name: "学习工具",
    count: 186,
    image:
      "/img_26.jpg",
  },
  {
    name: "创意工具",
    count: 157,
    image:
      "/img_31.jpg",
  },
  {
    name: "开发工具",
    count: 203,
    image:
      "/img_19.jpg",
  },
  {
    name: "休闲游戏",
    count: 312,
    image:
      "/img_15.jpg",
  },
  {
    name: "多人游戏",
    count: 175,
    image:
      "/img_13.jpg",
  },
];
// 成就数据
const achievements = [
  {
    title: "工具探索者",
    description: "使用了 10 个不同类别的工具",
    date: "2025-04-08",
    points: 50,
    icon: "Compass",
    bgColor: "bg-blue-100",
    iconColor: "text-blue-600",
  },
  {
    title: "游戏大师",
    description: "在 5 个不同游戏中获得高分",
    date: "2025-04-07",
    points: 100,
    icon: "Trophy",
    bgColor: "bg-yellow-100",
    iconColor: "text-yellow-600",
  },
  {
    title: "社区贡献者",
    description: "发布了 3 篇高质量评论",
    date: "2025-04-05",
    points: 30,
    icon: "ChatDotRound",
    bgColor: "bg-green-100",
    iconColor: "text-green-600",
  },
  {
    title: "连续使用",
    description: "连续 7 天登录平台",
    date: "2025-04-03",
    points: 70,
    icon: "Calendar",
    bgColor: "bg-purple-100",
    iconColor: "text-purple-600",
  },
];
// 排行榜数据
const leaderboard = [
  {
    name: "王大力",
    points: 8750,
    avatar:
      "/img_28.jpg",
  },
  {
    name: "李小云",
    points: 7620,
    avatar:
      "/img_5.jpg",
  },
  {
    name: "张明明",
    points: 6890,
    avatar:
      "/img_0.jpg",
  },
  {
    name: "赵小红",
    points: 5740,
    avatar:
      "/img_4.jpg",
  },
  {
    name: "刘天天",
    points: 4980,
    avatar:
      "/img_20.jpg",
  },
];
// 社区动态
const communityPosts = [
  {
    title: "如何高效使用我们的 AI 图片生成工具",
    content:
      "本文将详细介绍如何通过优化提示词，获得更好的 AI 图片生成效果，以及一些高级技巧和实用案例分享。",
    category: "教程",
    date: "2025-04-08",
    image:
      "/img_17.jpg",
    author: {
      name: "陈设计",
      avatar:
        "/img_6.jpg",
    },
    comments: 28,
    views: "3.5K",
  },
  {
    title: "2025 年最值得尝试的休闲小游戏推荐",
    content:
      "我们精选了 10 款最受欢迎的休闲游戏，从益智解谜到动作冒险，总有一款适合您在闲暇时光享受。",
    category: "推荐",
    date: "2025-04-07",
    image:
      "/img_27.jpg",
    author: {
      name: "李游戏",
      avatar:
        "/img_35.jpg",
    },
    comments: 42,
    views: "5.2K",
  },
  {
    title: "开发者故事：我如何创建一个月下载量破万的工具",
    content:
      "本文分享了一位独立开发者的成功经验，从创意构思到产品迭代，以及如何通过用户反馈持续优化产品。",
    category: "经验分享",
    date: "2025-04-06",
    image:
      "/img_29.jpg",
    author: {
      name: "王开发",
      avatar:
        "/img_23.jpg",
    },
    comments: 36,
    views: "4.8K",
  },
];
</script>
<style scoped>
/* 自定义样式 */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
/* 输入框样式覆盖 */
input:focus {
  outline: none;
}
/* 移除number输入框的箭头 */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input[type="number"] {
  -moz-appearance: textfield;
}
</style>
