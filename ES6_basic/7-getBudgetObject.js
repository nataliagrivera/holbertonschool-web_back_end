export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita,
  };

  Object.keys(budget).forEach(key => {
    budget[key] = `${budget[key]}` ;
  });

  return budget;
}
