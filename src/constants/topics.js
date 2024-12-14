export const DIFFICULTIES = ['easy', 'medium', 'hard'];

export const CATEGORIES = {
  ALL: 'all',
  WORK: 'work',
  HOBBIES: 'hobbies',
  TRAVEL: 'travel',
  ENTERTAINMENT: 'entertainment',
  FOOD: 'food',
  TECH: 'tech',
  LIFESTYLE: 'lifestyle'
};

export const getAllTopics = () => {
    const allTopics = {};
  
    // 각 카테고리별로
    Object.values(CATEGORIES).forEach(category => {
      if (category !== 'all') {  // 'all'은 제외
        try {
          // 각 난이도의 파일을 불러와서 합침
          allTopics[category] = DIFFICULTIES.reduce((acc, difficulty) => {
            const topicsFile = require(`../data/topics/${difficulty}/${category}.json`);
            return [...acc, ...topicsFile.topics];
          }, []);
        } catch (error) {
          console.error(`Error loading topics for category: ${category}`, error);
          allTopics[category] = [];
        }
      }
    });
  
    return allTopics;
  };

  export const getRandomTopic = (category) => {
    const allTopics = getAllTopics();
    
    if (category === CATEGORIES.ALL) {
      const allQuestions = Object.values(allTopics).flat();
      return allQuestions[Math.floor(Math.random() * allQuestions.length)];
    }
    
    const categoryTopics = allTopics[category];
    return categoryTopics[Math.floor(Math.random() * categoryTopics.length)];
  };

export const getTopicsByDifficulty = (difficulty) => {
  const result = {};
  
  Object.values(CATEGORIES).forEach(category => {
    if (category !== 'all') {
      try {
        const topicsFile = require(`../data/topics/${difficulty}/${category}.json`);
        result[category] = topicsFile.topics;
      } catch (error) {
        console.error(`Error loading topics for category: ${category}, difficulty: ${difficulty}`, error);
        result[category] = [];
      }
    }
  });

  return result;
};
  
  export const getTopicsByTags = (tags) => {
    const allTopics = getAllTopics();
    return Object.values(allTopics)
      .flat()
      .filter(topic => topic.tags.some(tag => tags.includes(tag)));
  };