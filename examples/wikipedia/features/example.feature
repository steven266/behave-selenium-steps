Feature: Step tests
	In order to show how to use these steps
	I want to give some examples

	Scenario: Search on Wikipedia
		Given I am on "search page"
        When I fill into "#powersearch"
        | selector           | value  |
        | input[name=search] | python |
        | input[name=ns14]   | 1      |
        and I submit "#powersearch"
        and I wait for "1" seconds
        Then I should have at least "1" ".searchresult" within ".searchresults"
        When I click on "ul.mw-search-results li:nth-child(1) a"
		and I wait for "1" seconds
		Then I should see "From Wikipedia, the free encyclopedia" within "html"
