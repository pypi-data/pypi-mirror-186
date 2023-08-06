# Package 
class STMatriClust:
  '''
  '''

  def __init__(self, pf,cf, multiple_datasets, dataset_names):
    ''' 
    pf: list of path(s) to spatial folder
    cf: list of path(s) to filtered_feature_matrix.h5
    multiple_datasets: boolean, if multiple datasets are being loaded 
    dataset_names: list of dataset names
    '''
    self.pf = pf 
    self.cf = cf 
    self.multiple_datasets = multiple_datasets
    self.dataset_names = dataset_names

    # Download matrisome data 
    if not os.path.isfile('matrisome_hs_masterlist.xls'): 
      print('Downloading matrisome data')
      !wget http://matrisomeproject.mit.edu/static/media/uploads/Files/Human%20in%20silico%20matrisome/matrisome_hs_masterlist.xls

    else:
      print('matrisome data already available')
    # Download basement membrane data 
    if not os.path.isfile('display.aspx?DocID=57554'): 
      print('Downloading basement membrane data')
      !wget https://documents.manchester.ac.uk/display.aspx?DocID=57554
    else:
      print('basement membrane data already available')

    # Load single dataset 
    if self.multiple_datasets == False: 
      print('Loading single dataset')
      self.adata = sc.read_visium(self.pf, genome=None, count_file=self.cf,  load_images=True,
                            source_image_path=None)
    else:
      print('Loading and merging multiple datasets ')
      # Load multiple datasets 
      self.adata_dict = {}
      for i in range(len(dataset_names)):
        self.adata_dict[self.dataset_names[i]] = sc.read_visium(self.pf[i], genome=None, count_file=self.cf[i], load_images=True,
                            source_image_path=None)
        self.adata_dict[self.dataset_names[i]].var_names_make_unique()

        
      # Merge adatas
      k = list(self.adata_dict.keys())
      adata_list = [self.adata_dict[i] for i in k[1:]]
      self.adata = self.adata_dict[k[0]].concatenate(
          (adata_list),
          batch_key='batch_id',
          uns_merge="unique",
          batch_categories=self.dataset_names
      )


  def quality_control(self, mt_p=20, gene_min_cell=10):
    '''
    mt_p:  percentage mitochrondial genes for removal 
    gene_min_cell: filter genes based on min cells
    '''
    print('calculating QC metrics ')
    self.adata.var["mt"] = self.adata.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(self.adata, qc_vars=["mt"], inplace=True)

    print('Removal of genes based on % mitochondrial ')
    # Remove based on mitochrondial genes 
    self.adata = self.adata[self.adata.obs["pct_counts_mt"] < mt_p]
    sc.pp.filter_genes(self.adata, min_cells=gene_min_cell)

    # Normalize data
    sc.pp.normalize_total(self.adata, inplace=True)
    sc.pp.log1p(self.adata)
    sc.pp.highly_variable_genes(self.adata, flavor="seurat", n_top_genes=2000)
  
  def correct_batch_effect(self):
    ''' Corrects batch effect using BKNN '''
    # Vizualize clusters before batch effect 
    print('------------------------------------------')
    print('Datasets BEFORE batch effect correction')
    sc.pp.neighbors(self.adata)
    sc.tl.umap(self.adata)
    sc.pl.umap(self.adata, color=['batch_id'],save= 'batch_effect.png')

    print('------------------------------------------')
    print('Datasets AFTER batch effect correction')
    # Correct batch effect and visualize 
    sc.external.pp.bbknn(self.adata, batch_key='batch_id') 
    sc.tl.umap(self.adata)
    sc.pl.umap(self.adata, color=['batch_id'], save='_corrected_be.png')

  def save_settings(self, savename): 
    '''
    name: directory all files will be saved within and prefix attached to saved files 
    '''
    self.savename = savename
    dir_name = self.savename+'_figures'
    if os.path.exists(dir_name):
      print('Directory already created, files will be saved over')
    else: 
      os.mkdir(dir_name)
      sc.settings.figdir ='/content/' + dir_name+'/'
      print('Image results will be saved in' , dir_name, 'folder')
    return 

  def cluster(self, all_genes=False):
    '''
    Cluster transcriptional spots 
    '''
    if all_genes == True:
      X = self.adata.obsm['X_pca']
    else:
      X = self.adata.X.toarray()
  # Find number of clusters in data 
    model = KElbowVisualizer(KMeans(), k=10)
    model.fit(X)
    model.show()
    opt_k = model.elbow_value_

    # Cluster using kmeans 
    km = KMeans(n_clusters=opt_k, random_state=0).fit(X) 
    self.adata.obs['kmeans'] = km.labels_.astype(str)

    # Plot top genes per cluster 
    sc.tl.rank_genes_groups(self.adata, 'kmeans', method='t-test')
    sc.pl.rank_genes_groups_dotplot(self.adata,n_genes=2, dendrogram = False, save = '_'+ self.savename, cmap = 'RdYlBu') 

  def visualize_clusters(self):
    lengths = [np.shape(self.adata_dict[i])[0] for i in self.adata_dict.keys()]
    km_labels = np.array(self.adata.obs['kmeans'].values)
    start = 0 
    for i in range(len(lengths)):
      self.adata_dict[self.dataset_names[i]].obs['kmeans'] = km_labels[start:(start+lengths[i])]
      start+= lengths[i]

    # Plot and visualize combined clusters back in original datasets 
    for k in self.dataset_names: 
      sc.pl.spatial(self.adata_dict[k], img_key="hires", color="kmeans",  palette ='RdYlBu', show=True, title=None, save='_' + self.savename+'_'+k+'.png', alpha_img=0) 
      plt.show()




  def filter_matrisome(self, category): 
    '''
    Filters either full matrisome, division  or categories 
    '''
    # Load matrisome list
    matrisome_list = pd.read_excel('/content/matrisome_hs_masterlist.xls')
    # Load basement membrane components 
    bm_df = pd.read_excel('/content/display.aspx?DocID=57554',header=9)
    # Select BM components 
    bm_df = bm_df[bm_df['Basement membrane component'] == 'Basement membrane component']

    # Check category or division is valid 
    valid_categories = ['Full matrisome', 
                        # Divisions 
                        'Matrisome-associated',
                        'Core matrisome',
                        # Categories 
                        'Collagens',
                        'ECM Glycoproteins',
                        'Proteoglycans',
                        'ECM-affiliated Proteins',
                        'ECM Regulators',
                        'Secreted Factors',
                        'Basement membrane']
    if category not in valid_categories:
      print('Incorrect category, select from: ', valid_categories)
      return 
    
    elif category == 'Basement membrane':
      matrisome_genes = bm_df['ACAN'].values

    # Matrisome 
    elif category == 'Full matrisome':
      matrisome_genes = matrisome_list['Gene Symbol'].to_list()
    elif category == 'Core matrisome':
      mask = matrisome_list['Division'] == category
      matrisome_genes = matrisome_list['Gene Symbol'][mask].to_list()

    elif category == 'Matrisome-associated':
      mask = matrisome_list['Division'] == category
      matrisome_genes = matrisome_list['Gene Symbol'][mask].to_list()
    else: 
      mask = matrisome_list['Category'] == category
      matrisome_genes = matrisome_list['Gene Symbol'][mask].to_list()


    var_df = sc.get.var_df(self.adata)
    vis_genes = var_df.index.to_list()
    def intersection(lst1, lst2):
      lst3 = [value for value in lst1 if value in lst2]
      return lst3
    mat_cis_intersect = intersection(vis_genes, matrisome_genes)
    mask = [vg in mat_cis_intersect for vg in vis_genes]
    self.adata = self.adata[:, mask]
    print(category, 'detected: ', np.shape(self.adata)[1],'/',len(matrisome_genes))
    return 


  


  
