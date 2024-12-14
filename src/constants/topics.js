import workTopics from '../data/topics/work.json';
import hobbiesTopics from '../data/topics/hobbies.json';

export const CATEGORIES = {
  ALL: 'all',
  WORK: 'work',
  HOBBIES: 'hobbies'
};

export const getAllTopics = () => {
  const allTopics = {
    [CATEGORIES.WORK]: workTopics.topics,
    [CATEGORIES.HOBBIES]: hobbiesTopics.topics,
  };
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