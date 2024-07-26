function searchGames() {
    const searchInput = document.querySelector('.search');
    const searchText = searchInput.value.toLowerCase();
    const gameBlocks = document.querySelectorAll('.block');
  
    gameBlocks.forEach(block => {
      const gameName = block.querySelector('h3').textContent.toLowerCase();
      if (gameName.includes(searchText)) {
        block.style.display = 'block';
      } else {
        block.style.display = 'none';
      }
    });
  }

function openGamePage(id) {
    // Формируем URL страницы игры
    let gamePageUrl = `/game_page/${id}`;
    
    // Перенаправляем пользователя на страницу игры
    window.location.href = gamePageUrl;
  }


function searchDates() {
    const searchInput = document.querySelector('.search_date');
    const searchDate = searchInput.value.toLowerCase();
    const gameBlocks = document.querySelectorAll('.block');
  
    gameBlocks.forEach(block => {
      const gameDate = block.querySelector('.date').textContent.toLowerCase();
      if (gameDate.includes(searchDate)) {
        block.style.display = 'block';
      } else {
        block.style.display = 'none';
      }
    });
  }

function searchCategory() {
    const searchInput = document.querySelector('.search_category');
    const searchCategory = searchInput.value.toLowerCase();
    const gameBlocks = document.querySelectorAll('.block');
  
    gameBlocks.forEach(block => {
      const gameCategory = block.querySelector('.category').textContent.toLowerCase();
      if (gameCategory.includes(searchCategory)) {
        block.style.display = 'block';
      } else {
        block.style.display = 'none';
      }
    });
  }


  const inputField = document.getElementById('input-field');
  const suggestionsList = document.getElementById('suggestions-list');

  inputField.addEventListener('focus', () => {
    suggestionsList.style.display = 'block';
  });

  inputField.addEventListener('blur', () => {
    suggestionsList.style.display = 'none';
  });

  const suggestions = document.querySelectorAll('#suggestions-list li');
  suggestions.forEach(suggestion => {
    suggestion.addEventListener('click', () => {
      inputField.value = suggestion.textContent;
      suggestionsList.style.display = 'none';
    });
  });