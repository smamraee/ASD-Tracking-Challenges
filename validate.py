import motmetrics as mm
import pandas as pd

def read_labels(file_path):
    """
    Reads MOTChallenge-format labels from a text file into a DataFrame.
    """
    columns = ['frame', 'id', 'bb_left', 'bb_top', 'bb_width', 'bb_height', 'conf', 'class']
    data = pd.read_csv(file_path, header=None, names=columns, index_col=False)
    return data[['frame', 'id', 'bb_left', 'bb_top', 'bb_width', 'bb_height']]

def compute_metrics(gt_path, pred_path):
    """
    Computes MOTA, IDF1, and IDS using motmetrics.
    """
    # Initialize metrics accumulator
    acc = mm.MOTAccumulator(auto_id=True)
    
    # Read ground truth and prediction labels
    gt = read_labels(gt_path)
    pred = read_labels(pred_path)
    
    # Iterate over frames
    for frame in sorted(gt['frame'].unique()):
        # Ground truth for the current frame
        gt_frame = gt[gt['frame'] == frame]
        gt_ids = gt_frame['id'].values
        gt_boxes = gt_frame[['bb_left', 'bb_top', 'bb_width', 'bb_height']].values
        
        # Predictions for the current frame
        pred_frame = pred[pred['frame'] == frame]
        pred_ids = pred_frame['id'].values
        pred_boxes = pred_frame[['bb_left', 'bb_top', 'bb_width', 'bb_height']].values
        
        # Compute distances (IoU or any metric you prefer)
        distances = mm.distances.iou_matrix(gt_boxes, pred_boxes, max_iou=0.5)
        
        # Update accumulator
        acc.update(gt_ids, pred_ids, distances)
    
    # Compute metrics
    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=['mota', 'idf1', 'num_switches'], name='metrics')
    
    # Extract metrics
    mota = summary.loc['metrics']['mota']
    idf1 = summary.loc['metrics']['idf1']
    ids = summary.loc['metrics']['num_switches']
    
    return mota, idf1, ids

# Example usage
gt_path = "ground_truth.txt"  # Replace with your ground truth file path
pred_path = "predictions.txt"  # Replace with your predictions file path

mota, idf1, ids = compute_metrics(gt_path, pred_path)
print(f"MOTA: {mota:.2f}, IDF1: {idf1:.2f}, IDS: {ids}")
