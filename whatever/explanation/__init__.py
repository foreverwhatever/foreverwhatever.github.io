
# coding: utf-8

# In[23]:

from toolz.curried import *
import pandas, sklearn.tree
__all__ = ['Describer', 'nx_tree']


# In[24]:

def nx_tree(clf):
    """
    Describe a decision tree using the sklearn view.
    http://scikit-learn.org/stable/modules/tree.html#classification
    
    IPython.display.Image(nx_tree(clf).create_png())  
    
    """
    import pydotplus
    dot_data = sklearn.tree.export_graphviz(
        clf,
        out_file=None, #'described_features.dot', 
        class_names=clf.classes_.astype(str),
    #     feature_names=None,
        filled=True, rounded=True,  
        special_characters=True,
    )
    return pydotplus.graph_from_dot_data(dot_data)  
    


# In[26]:

class Describer(sklearn.tree.DecisionTreeClassifier):
    """
    Adds an attribute treeframe_ that is a dataframe of the decision properties.
    """
    def tree_to_dataframe(self):
        attr = {}
        for attr_name in dir(self.tree_):
            tree_attr = getattr(self.tree_, attr_name)
            if hasattr(tree_attr, 'shape') and tree_attr.shape[0] == len(self.tree_.feature):
                attr[attr_name] = tree_attr.tolist()
        self.treeframe_ = pandas.DataFrame(attr)
        self.treeframe_.index= self.treeframe_.index.rename('source')

        self.treeframe_.value = self.treeframe_.value.apply(first)

        assert not (
            self.treeframe_
            .children_left
            .isin(self.treeframe_.children_right)
            [self.treeframe_.children_left>-1]
            .any()
        )
        return self
    
    def discover_common_paths(self, X, y):
        paths = self.decision_path(X).tocoo()
        

        common_paths = pipe(
            zip(paths.row, paths.col),
            groupby(first),
            valmap(map(second)),
            valmap(tuple),
            pandas.Series,
        ).groupby(y).apply(
            lambda s: s.value_counts().iloc[[0]].index[0]
        )
    
        ordered_tree = (
            self.treeframe_
            .loc[
                pipe(
                    common_paths.tolist(), concat, list
                )
            ].copy()
        )

        ordered_tree['condition'] = ''
        ordered_tree['condition'] += (
            pandas.Index(
                ordered_tree
                .index
                .isin(ordered_tree.children_right)
                
            ).map(['','>'].__getitem__)
        )
        ordered_tree['condition'] += (
            pandas.Index(
                ordered_tree
                .index
                .isin(ordered_tree.children_left)
            ).map(['','<'].__getitem__)
        )
        
        ordered_tree['class'] = (ordered_tree.index==0).cumsum() - 1

        ordered_tree['class'] = ordered_tree['class'].apply(
            common_paths.index.__getitem__
        )
                
        return ordered_tree 
    
    def why(self, X, y):
        paths = (
            self
            .fit(X, y)
            .tree_to_dataframe()
            .discover_common_paths(X, y)
        )
        paths = pandas.concat([
            paths['feature'].iloc[:-1].reset_index(drop=True), 
            paths.iloc[1:]['condition'].reset_index(drop=True),
            paths['threshold'].iloc[:-1].reset_index(drop=True), 
            paths.iloc[1:]['class'].reset_index(drop=True),
        ], axis=1).set_index('class')
        return paths[paths.condition != '']


# In[ ]:



