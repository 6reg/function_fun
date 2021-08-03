let countries = 
	['Osterreich', 'Andorra', 'Vietnam'];

const sorter = (x = ['USA']) => x.sort((a,b) => a > b ? 1: -1)

const sorter1 = (x = ['Canada']) => x.sort((a,b) => a.localeCompare(b))


console.log(sorter(countries), '\n', sorter1(countries), '\n', sorter())
